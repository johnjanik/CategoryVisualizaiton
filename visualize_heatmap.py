import importlib.util
import os
import sys
import re
import datetime
import math
try:
    import numpy as np
except ImportError:
    print('numpy is required. Please install it with `pip install numpy`.')
    sys.exit(1)
try:
    import pandas as pd
except ImportError:
    print('pandas is required. Please install it with `pip install pandas`.')
    sys.exit(1)
try:
    import matplotlib.pyplot as plt
except ImportError:
    print('matplotlib is required. Please install it with `pip install matplotlib`.')
    sys.exit(1)
try:
    import seaborn as sns
except ImportError:
    print('seaborn is required. Please install it with `pip install seaborn`.')
    sys.exit(1)
try:
    from matplotlib.colors import ListedColormap, BoundaryNorm
except ImportError:
    print('matplotlib.colors is required. Please install matplotlib.')
    sys.exit(1)
try:
    import networkx as nx
except ImportError:
    print('networkx is required. Please install it with `pip install networkx`.')
    sys.exit(1)

# Path to the data file
DATA_PATH = 'heat_map_data.py'
MINMAP_PATH = 'category-theory-mindmap.md'

# Dynamically import the .md file as a Python module
spec = importlib.util.spec_from_file_location('heat_map_data', DATA_PATH)
if spec is None or spec.loader is None:
    raise ImportError(f'Could not load spec from {DATA_PATH}. Is the file present and valid?')
data_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(data_module)
results = data_module.results

# Emoji to value and color mapping
EMOJI_TO_VALUE = {
    '✅': 3,
    '🟡': 2,
    '⚠️': 1,
    '❌': 0,
    'N/A': np.nan,
}
EMOJI_TO_COLOR = {
    3: '#4CAF50',   # Green
    2: '#FFEB3B',   # Yellow
    1: '#FF9800',   # Orange
    0: '#F44336',   # Red
    # nan handled in colormap
}

# Extract all concepts, agents, reviewers
concepts = list(results.keys())
agents = list(next(iter(results.values())).keys())
reviewers = list(list(next(iter(results.values())).values())[0].keys())

# Build a 3D DataFrame: index=(concept, agent, reviewer), value=emoji
records = []
for concept, agent_dict in results.items():
    for agent, reviewer_dict in agent_dict.items():
        for reviewer, emoji in reviewer_dict.items():
            records.append({
                'Concept': concept,
                'Agent': agent,
                'Reviewer': reviewer,
                'Emoji': emoji,
                'Value': EMOJI_TO_VALUE.get(emoji, np.nan),
            })
df = pd.DataFrame(records)

def unique_filename(prefix):
    now = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    return f'{prefix}_{now}.png'

# Helper to plot a slice
def plot_slice(df, by='Agent', name=None, save_path=None):
    if by == 'Agent':
        # Slice: all concepts for a given agent (Reviewer on x-axis)
        data = df[df['Agent'] == name].pivot(index='Concept', columns='Reviewer', values='Value')
        title = f'Heatmap for Agent: {name}'
        annot = df[df['Agent']==name].pivot(index='Concept', columns='Reviewer', values='Emoji')
    elif by == 'Reviewer':
        # Slice: all concepts for a given reviewer (Agent on x-axis)
        data = df[df['Reviewer'] == name].pivot(index='Concept', columns='Agent', values='Value')
        title = f'Heatmap for Reviewer: {name}'
        annot = df[df['Reviewer']==name].pivot(index='Concept', columns='Agent', values='Emoji')
    else:
        raise ValueError('by must be "Agent" or "Reviewer"')

    # Custom colormap: green, yellow, orange, red, gray for nan
    cmap = ListedColormap([
        EMOJI_TO_COLOR[0],
        EMOJI_TO_COLOR[1],
        EMOJI_TO_COLOR[2],
        EMOJI_TO_COLOR[3],
        '#BDBDBD', # Gray for nan
    ])
    bounds = [-0.5, 0.5, 1.5, 2.5, 3.5, 4.5]
    norm = BoundaryNorm(bounds, cmap.N)

    plt.figure(figsize=(8, max(6, len(data) * 0.3)))
    ax = sns.heatmap(
        data,
        cmap=cmap,
        norm=norm,
        linewidths=0.5,
        linecolor='white',
        cbar=False,
        square=False,
        annot=annot,
        fmt='',
        mask=data.isnull(),
    )
    plt.title(title)
    plt.tight_layout()
    if not save_path:
        save_path = unique_filename(f'heatmap_{by}_{name}')
    plt.savefig(save_path)
    print(f'Saved heatmap to {save_path}')
    plt.close()

def get_term_flag_status(concept, results):
    """Return the most severe flag for a concept across all agents/reviewers."""
    severity = {'❌': 3, '⚠️': 2, '🟡': 1, '✅': 0, 'N/A': -1}
    max_severity = 0
    max_flag = '✅'
    for agent_dict in results[concept].values():
        for emoji in agent_dict.values():
            if emoji in severity and severity[emoji] > max_severity:
                max_severity = severity[emoji]
                max_flag = emoji
    return max_flag

def plot_mindmap(results, save_path=None):
    # Build a simple mindmap: root -> concept
    G = nx.DiGraph()
    root = 'Category Theory Terms'
    G.add_node(root)
    color_map = {}
    node_labels = {root: root}
    # Color mapping for mindmap
    mindmap_colors = {
        '❌': '#F44336',   # Red
        '⚠️': '#FF9800',   # Orange
        '🟡': '#FFEB3B',   # Yellow
        '✅': '#4CAF50',   # Green
        'N/A': '#BDBDBD', # Gray
    }
    for concept in results:
        flag = get_term_flag_status(concept, results)
        G.add_node(concept)
        G.add_edge(root, concept)
        color_map[concept] = mindmap_colors.get(flag, '#4CAF50')
        node_labels[concept] = concept
    color_map[root] = '#4CAF50'  # Default color for root
    # Layout
    pos = nx.spring_layout(G, k=2, center=(0,0))
    plt.figure(figsize=(16, 12))
    nx.draw(G, pos, with_labels=False, arrows=False, node_color=[color_map.get(n, '#4CAF50') for n in G.nodes], node_size=600, edge_color='#888')
    nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=8)
    plt.title('Mindmap of Category Theory Terms (flagged by heatmap status)')
    plt.axis('off')
    plt.tight_layout()
    if not save_path:
        save_path = unique_filename('mindmap')
    plt.savefig(save_path)
    print(f'Saved mindmap to {save_path}')
    plt.close()

def parse_mindmap_markdown(filepath):
    """Parse the mindmap markdown file into a tree structure, ensuring list items are always children of the most recent heading at the correct depth."""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    tree = None
    stack = []  # (node, depth)
    heading_nodes = {}  # depth -> node
    for line in lines:
        line = line.rstrip('\n')
        if not line.strip():
            continue  # skip blank lines
        heading_match = re.match(r'^(#+) (.+)', line)
        list_match = re.match(r'^([ \t]*)[-*] (.+)', line)
        if heading_match:
            depth = len(heading_match.group(1))
            label = heading_match.group(2).strip()
            node = {'label': label, 'children': []}
            heading_nodes[depth] = node
            # Remove deeper headings from heading_nodes
            for d in list(heading_nodes.keys()):
                if d > depth:
                    del heading_nodes[d]
            if depth == 1:
                tree = node
                stack = [(node, depth)]
            else:
                # Attach to parent heading at depth-1
                parent = heading_nodes.get(depth - 1)
                if parent:
                    parent['children'].append(node)
                stack.append((node, depth))
            # Remove any stack nodes deeper than current
            while stack and stack[-1][1] >= depth:
                stack.pop()
            stack.append((node, depth))
        elif list_match:
            label = list_match.group(2).strip()
            # Attach to the most recent heading (highest depth)
            if heading_nodes:
                parent_depth = max(heading_nodes.keys())
                parent = heading_nodes[parent_depth]
                node = {'label': label, 'children': []}
                parent['children'].append(node)
    return tree

def get_most_severe_flag(term, results):
    """Return the most severe flag for a term across all agents/reviewers."""
    severity = {'❌': 3, '⚠️': 2, '🟡': 1, '✅': 0, 'N/A': -1}
    max_severity = 0
    max_flag = '✅'
    if term in results:
        for agent_dict in results[term].values():
            for emoji in agent_dict.values():
                if emoji in severity and severity[emoji] > max_severity:
                    max_severity = severity[emoji]
                    max_flag = emoji
    return max_flag

def build_mindmap_graph(node, results, G=None, parent=None, color_map=None, label_map=None):
    if G is None:
        G = nx.DiGraph()
    if color_map is None:
        color_map = {}
    if label_map is None:
        label_map = {}
    label = node['label']
    flag = get_most_severe_flag(label, results)
    mindmap_colors = {
        '❌': '#F44336',   # Red
        '⚠️': '#FF9800',   # Orange
        '🟡': '#FFEB3B',   # Yellow
        '✅': '#4CAF50',   # Green
        'N/A': '#BDBDBD', # Gray
    }
    G.add_node(label)
    color_map[label] = mindmap_colors.get(flag, '#4CAF50')
    label_map[label] = label
    if parent:
        G.add_edge(parent, label)
    for child in node.get('children', []):
        build_mindmap_graph(child, results, G, label, color_map, label_map)
    return G, color_map, label_map

def get_tree_layers(node, depth=0, layers=None):
    if layers is None:
        layers = {}
    if depth not in layers:
        layers[depth] = []
    layers[depth].append(node['label'])
    for child in node.get('children', []):
        get_tree_layers(child, depth+1, layers)
    return layers

def get_label_to_parent(node, parent=None, mapping=None):
    if mapping is None:
        mapping = {}
    mapping[node['label']] = parent
    for child in node.get('children', []):
        get_label_to_parent(child, node['label'], mapping)
    return mapping

def custom_layered_layout(tree):
    layers = get_tree_layers(tree)
    label_to_depth = {}
    for depth, nodes in layers.items():
        for n in nodes:
            label_to_depth[n] = depth
    max_width = max(len(nodes) for nodes in layers.values())
    pos = {}
    for depth, nodes in layers.items():
        n_nodes = len(nodes)
        for i, label in enumerate(nodes):
            # Spread nodes evenly along x-axis, y by depth
            x = (i + 1) * (max_width + 1) / (n_nodes + 1)
            y = -depth * 2  # negative so root is at top
            pos[label] = (x, y)
    return pos

def get_tree_structure(node, depth=0, nodes=None, edges=None, parent=None):
    if nodes is None:
        nodes = []
    if edges is None:
        edges = []
    nodes.append((node['label'], depth))
    if parent:
        edges.append((parent, node['label']))
    for child in node.get('children', []):
        get_tree_structure(child, depth+1, nodes, edges, node['label'])
    return nodes, edges

def radial_web_layout(tree, base_radius=2, leaf_cluster_factor=0.3, angle_stagger=0.04):
    nodes, _ = get_tree_structure(tree)
    # Group nodes by depth
    depth_dict = {}
    for label, depth in nodes:
        if depth not in depth_dict:
            depth_dict[depth] = []
        depth_dict[depth].append(label)
    max_depth = max(depth_dict.keys())
    pos = {}
    # Assign angles for each node at each depth
    def assign_angles(node, depth, angle_start, angle_end, sibling_idx=0):
        children = node.get('children', [])
        label = node['label']
        if not children:
            # Leaf: cluster more tightly
            angle = (angle_start + angle_end) / 2
            # Stagger angle for readability
            angle += ((-1) ** sibling_idx) * angle_stagger * (sibling_idx // 2)
            radius = base_radius + math.exp(depth) + leaf_cluster_factor * (math.exp(max_depth) - math.exp(depth))
            pos[label] = (
                radius * math.cos(angle),
                radius * math.sin(angle)
            )
            return [angle]
        else:
            n = len(children)
            angles = []
            for i, child in enumerate(children):
                child_angle_start = angle_start + (angle_end - angle_start) * i / n
                child_angle_end = angle_start + (angle_end - angle_start) * (i + 1) / n
                child_angles = assign_angles(child, depth+1, child_angle_start, child_angle_end, i)
                angles.extend(child_angles)
            mean_angle = sum(angles) / len(angles)
            radius = base_radius + math.exp(depth)
            pos[label] = (
                radius * math.cos(mean_angle),
                radius * math.sin(mean_angle)
            )
            return angles
    assign_angles(tree, 0, 0, 2 * math.pi)
    return pos

def plot_combined_mindmap_heatmap(mindmap_path, results, save_path=None, layout='spring'):
    tree = parse_mindmap_markdown(mindmap_path)
    G, color_map, label_map = build_mindmap_graph(tree, results)
    if layout == 'hierarchical':
        try:
            from networkx.drawing.nx_agraph import graphviz_layout
            pos = graphviz_layout(G, prog='dot')
        except ImportError:
            print('pygraphviz or pydot is required for hierarchical layout. Falling back to spring layout.')
            pos = nx.spring_layout(G, k=4, center=(0,0), iterations=200)
    elif layout == 'layered':
        pos = custom_layered_layout(tree)
    elif layout == 'web':
        pos = radial_web_layout(tree)
    else:
        pos = nx.spring_layout(G, k=4, center=(0,0), iterations=200)
    # Make the image very large for readability
    plt.figure(figsize=(60, 60))
    nx.draw(
        G, pos,
        with_labels=False,
        arrows=False,
        node_color=[color_map.get(n, '#4CAF50') for n in G.nodes],
        node_size=1800,
        edge_color='#888',
        linewidths=1.5
    )
    nx.draw_networkx_labels(G, pos, labels=label_map, font_size=18, font_weight='bold')
    plt.title('Combined Mindmap + Heatmap of Category Theory Terms', fontsize=28)
    plt.axis('off')
    plt.tight_layout()
    if not save_path:
        save_path = unique_filename('combined_mindmap_heatmap')
    plt.savefig(save_path, dpi=200)
    print(f'Saved combined mindmap+heatmap to {save_path}')
    svg_path = save_path.rsplit('.', 1)[0] + '.svg'
    plt.savefig(svg_path, format='svg')
    print(f'Saved combined mindmap+heatmap to {svg_path}')
    plt.close()

def print_mindmap_tree(node, depth=0):
    print('  ' * depth + '- ' + node['label'])
    for child in node.get('children', []):
        print_mindmap_tree(child, depth + 1)

# Interactive CLI

def main():
    while True:
        print('\nSelect visualization type:')
        print('1. Heatmap by Agent')
        print('2. Heatmap by Reviewer')
        print('3. Mindmap of Terms')
        print('4. Combined Mindmap + Heatmap')
        print('5. Print Mindmap Tree Structure')
        print('6. Exit')
        choice = input('Enter choice: ').strip()
        if choice == '1':
            print('\nAvailable Agents:')
            for i, agent in enumerate(agents):
                print(f'{i+1}. {agent}')
            idx = input('Select Agent by number: ').strip()
            if not idx.isdigit() or not (1 <= int(idx) <= len(agents)):
                print('Invalid selection.')
                continue
            agent = agents[int(idx)-1]
            plot_slice(df, by='Agent', name=agent)
        elif choice == '2':
            print('\nAvailable Reviewers:')
            for i, reviewer in enumerate(reviewers):
                print(f'{i+1}. {reviewer}')
            idx = input('Select Reviewer by number: ').strip()
            if not idx.isdigit() or not (1 <= int(idx) <= len(reviewers)):
                print('Invalid selection.')
                continue
            reviewer = reviewers[int(idx)-1]
            plot_slice(df, by='Reviewer', name=reviewer)
        elif choice == '3':
            plot_mindmap(results)
        elif choice == '4':
            layout_short = input("Choose layout for combined mindmap+heatmap (s for 'spring', h for 'hierarchical', l for 'layered', w for 'web'): ").strip().lower()
            if layout_short == 'h':
                layout = 'hierarchical'
            elif layout_short == 'l':
                layout = 'layered'
            elif layout_short == 'w':
                layout = 'web'
            else:
                layout = 'spring'
            plot_combined_mindmap_heatmap(MINMAP_PATH, results, layout=layout)
        elif choice == '5':
            tree = parse_mindmap_markdown(MINMAP_PATH)
            print_mindmap_tree(tree)
        elif choice == '6':
            print('Exiting.')
            break
        else:
            print('Invalid choice.')

if __name__ == '__main__':
    main() 