## Classical Category Theory

### Abelian category
An abelian category is a pre-abelian category $\mathcal{A}$ satisfying:
- Every monomorphism is a kernel of some morphism
- Every epimorphism is a cokernel of some morphism
- Every morphism can be factored as an epimorphism followed by a monomorphism

### Additive category
An additive category is a category $\mathcal{C}$ enriched over abelian groups such that:
- $\mathcal{C}$ has a zero object $0$
- $\mathcal{C}$ has all finite biproducts (equivalently, all finite products and coproducts that coincide)

### Adjoint functor theorem
**Freyd's General Adjoint Functor Theorem**: A functor $G: \mathcal{D} \to \mathcal{C}$ has a left adjoint if and only if:
1. $G$ preserves all limits that exist in $\mathcal{D}$
2. For each $c \in \mathcal{C}$, the comma category $(c \downarrow G)$ satisfies the solution set condition

### Adjunction
An adjunction consists of functors $L: \mathcal{C} \rightleftarrows \mathcal{D} : R$ with natural isomorphism:
$$\text{Hom}_{\mathcal{D}}(L(c), d) \cong \text{Hom}_{\mathcal{C}}(c, R(d))$$
The unit $\eta: \text{id}_\mathcal{C} \Rightarrow R \circ L$ and counit $\epsilon: L \circ R \Rightarrow \text{id}_\mathcal{D}$ satisfy the triangle identities.

### Automorphism
An automorphism of an object $X$ in a category $\mathcal{C}$ is an isomorphism $f: X \to X$.

### Balanced category
A category $\mathcal{C}$ is balanced if every morphism that is both monic and epic is an isomorphism.

### Category
A category $\mathcal{C}$ consists of:
- A collection $\text{Ob}(\mathcal{C})$ of objects
- For each pair $(A,B)$ of objects, a collection $\text{Hom}_\mathcal{C}(A,B)$ of morphisms
- Composition $\circ: \text{Hom}(B,C) \times \text{Hom}(A,B) \to \text{Hom}(A,C)$
- Identity morphisms $\text{id}_A: A \to A$

satisfying associativity and unit laws. Small if $\text{Ob}(\mathcal{C})$ is a set; locally small if each $\text{Hom}(A,B)$ is a set.

### Category of elements
For a functor $F: \mathcal{C} \to \mathbf{Set}$, the category of elements $\int F$ has:
- Objects: pairs $(c, x)$ where $c \in \mathcal{C}$ and $x \in F(c)$
- Morphisms $(c, x) \to (d, y)$: morphisms $f: c \to d$ such that $F(f)(x) = y$

### Cauchy (Karoubi) completion
The Cauchy completion $\overline{\mathcal{C}}$ of a category $\mathcal{C}$ has:
- Objects: idempotents $(e: A \to A)$ in $\mathcal{C}$
- Morphisms $(e: A \to A) \to (e': B \to B)$: morphisms $f: A \to B$ such that $f = e' \circ f \circ e$

### Comma category
For functors $F: \mathcal{A} \to \mathcal{C}$ and $G: \mathcal{B} \to \mathcal{C}$, the comma category $(F \downarrow G)$ has:
- Objects: triples $(a, f, b)$ where $a \in \mathcal{A}$, $b \in \mathcal{B}$, and $f: F(a) \to G(b)$
- Morphisms $(a, f, b) \to (a', f', b')$: pairs $(h: a \to a', k: b \to b')$ making the obvious square commute

### Composition
Composition in a category is the operation $\circ: \text{Hom}(B,C) \times \text{Hom}(A,B) \to \text{Hom}(A,C)$ satisfying:
- Associativity: $(h \circ g) \circ f = h \circ (g \circ f)$
- Identity laws: $f \circ \text{id}_A = f = \text{id}_B \circ f$ for $f: A \to B$

### Contravariant functor
A contravariant functor $F: \mathcal{C} \to \mathcal{D}$ is a functor $F: \mathcal{C}^{op} \to \mathcal{D}$, reversing the direction of morphisms.

### Copower
The copower of an object $A$ by a set $S$, denoted $S \cdot A$, is the coproduct $\coprod_{s \in S} A$.

### Copresheaf
A copresheaf on $\mathcal{C}$ is a functor $F: \mathcal{C} \to \mathbf{Set}$.

### Coproduct
The coproduct $\coprod_{i \in I} A_i$ is the colimit of the discrete diagram $\{A_i\}_{i \in I}$, with injections $\iota_j: A_j \to \coprod_{i \in I} A_i$.

### Cosegment
A cosegment object is an object $X$ with two morphisms $s, t: \ast \to X$ from the terminal object.

### Coslice category
The coslice category $c/\mathcal{C}$ for $c \in \mathcal{C}$ has:
- Objects: morphisms $f: c \to d$ in $\mathcal{C}$
- Morphisms: commutative triangles

### Coequalizer
The coequalizer of $f, g: A \rightrightarrows B$ is the colimit of this diagram, giving $q: B \to C$ with $q \circ f = q \circ g$ universal.

### Coefficient
In enriched category theory, coefficients refer to the enriching category $\mathcal{V}$.

### Coend
For a functor $F: \mathcal{C}^{op} \times \mathcal{C} \to \mathcal{D}$, the coend is:
$$\int^{c \in \mathcal{C}} F(c,c) = \text{coeq}\left(\coprod_{f: c \to c'} F(c',c) \rightrightarrows \coprod_{c} F(c,c)\right)$$

### Coreflective subcategory
A full subcategory $\mathcal{D} \hookrightarrow \mathcal{C}$ is coreflective if the inclusion has a right adjoint.

### Covariant functor
A covariant functor $F: \mathcal{C} \to \mathcal{D}$ preserves the direction of morphisms: $F(f: A \to B) = F(f): F(A) \to F(B)$.

### Dinatural transformation
A dinatural transformation $\alpha: F \Rightarrow G$ between functors $F, G: \mathcal{C}^{op} \times \mathcal{C} \to \mathcal{D}$ consists of components $\alpha_c: F(c,c) \to G(c,c)$ satisfying the hexagon identity.

### Dual category
The dual (opposite) category $\mathcal{C}^{op}$ has the same objects as $\mathcal{C}$ with $\text{Hom}_{\mathcal{C}^{op}}(A,B) = \text{Hom}_\mathcal{C}(B,A)$.

### End
For a functor $F: \mathcal{C}^{op} \times \mathcal{C} \to \mathcal{D}$, the end is:
$$\int_{c \in \mathcal{C}} F(c,c) = \text{eq}\left(\prod_{c} F(c,c) \rightrightarrows \prod_{f: c \to c'} F(c',c)\right)$$

### Equalizer
The equalizer of $f, g: A \rightrightarrows B$ is the limit of this diagram, giving $e: E \to A$ with $f \circ e = g \circ e$ universal.

### Essentially surjective functor
A functor $F: \mathcal{C} \to \mathcal{D}$ is essentially surjective if for every $d \in \mathcal{D}$, there exists $c \in \mathcal{C}$ with $F(c) \cong d$.

### Exact category
An exact category is an additive category with a class of short exact sequences satisfying the axioms of Quillen.

### Factorization system
A factorization system $(\mathcal{E}, \mathcal{M})$ on $\mathcal{C}$ consists of classes of morphisms such that:
- Every morphism factors as $f = m \circ e$ with $e \in \mathcal{E}$, $m \in \mathcal{M}$
- $\mathcal{E}$ and $\mathcal{M}$ satisfy the unique diagonal fill-in property

### Fully faithful functor
A functor $F: \mathcal{C} \to \mathcal{D}$ is fully faithful if each function $F_{A,B}: \text{Hom}_\mathcal{C}(A,B) \to \text{Hom}_\mathcal{D}(F(A),F(B))$ is bijective.

### Functor
A functor $F: \mathcal{C} \to \mathcal{D}$ consists of:
- Object function $F: \text{Ob}(\mathcal{C}) \to \text{Ob}(\mathcal{D})$
- Morphism functions $F_{A,B}: \text{Hom}_\mathcal{C}(A,B) \to \text{Hom}_\mathcal{D}(F(A),F(B))$
preserving composition and identities.

### Functor category
The functor category $[\mathcal{C}, \mathcal{D}]$ has functors $F: \mathcal{C} \to \mathcal{D}$ as objects and natural transformations as morphisms.

### Full functor
A functor $F: \mathcal{C} \to \mathcal{D}$ is full if each function $F_{A,B}: \text{Hom}_\mathcal{C}(A,B) \to \text{Hom}_\mathcal{D}(F(A),F(B))$ is surjective.

### Grothendieck fibration
A functor $p: \mathcal{E} \to \mathcal{B}$ is a Grothendieck fibration if for every $e \in \mathcal{E}$ and morphism $f: b \to p(e)$ in $\mathcal{B}$, there exists a cartesian lifting of $f$ at $e$.

### Grothendieck topology
A Grothendieck topology on $\mathcal{C}$ assigns to each object $c$ a collection $J(c)$ of sieves (covering families) satisfying stability, transitivity, and identity axioms.

### Image
The image of $f: A \to B$ is the smallest subobject of $B$ through which $f$ factors.

### Initial object
An object $0 \in \mathcal{C}$ is initial if for every object $A$, there exists a unique morphism $0 \to A$.

### Isomorphism
A morphism $f: A \to B$ is an isomorphism if there exists $g: B \to A$ with $g \circ f = \text{id}_A$ and $f \circ g = \text{id}_B$.

### Kan extension
The left Kan extension of $F: \mathcal{C} \to \mathcal{E}$ along $K: \mathcal{C} \to \mathcal{D}$ is the left adjoint to the restriction functor $[\mathcal{D}, \mathcal{E}] \to [\mathcal{C}, \mathcal{E}]$ given by precomposition with $K$.

### Kernel
The kernel of $f: A \to B$ in an abelian category is the equalizer of $f$ and the zero morphism $0: A \to B$.

### Lawvere theory
A Lawvere theory is a small category $\mathcal{T}$ with finite products and a strict finite-product-preserving functor $\mathcal{F}^{op} \to \mathcal{T}$ from the opposite of the category of finite sets.

### Limit
The limit of a functor $F: \mathcal{J} \to \mathcal{C}$ is an object $\lim F$ with a cone $\pi_j: \lim F \to F(j)$ universal among all cones over $F$.

### Locally presentable category
A category $\mathcal{C}$ is locally presentable if it is cocomplete and has a set of $\kappa$-compact objects generating $\mathcal{C}$ under $\kappa$-filtered colimits for some regular cardinal $\kappa$.

### Monomorphism
A morphism $f: A \to B$ is a monomorphism if $f \circ g = f \circ h$ implies $g = h$ for all $g, h: C \to A$.

### Multicategory
A multicategory has objects and multimorphisms $(A_1, \ldots, A_n) \to B$ with composition and identities satisfying appropriate axioms.

### Natural transformation
A natural transformation $\alpha: F \Rightarrow G$ between functors $F, G: \mathcal{C} \to \mathcal{D}$ consists of components $\alpha_c: F(c) \to G(c)$ such that for all $f: c \to c'$, we have $G(f) \circ \alpha_c = \alpha_{c'} \circ F(f)$.

### Natural isomorphism
A natural transformation $\alpha: F \Rightarrow G$ is a natural isomorphism if each component $\alpha_c$ is an isomorphism.

### Nerve of a category
The nerve $N(\mathcal{C})$ of a category $\mathcal{C}$ is the simplicial set with $N(\mathcal{C})_n$ = composable sequences of $n$ morphisms in $\mathcal{C}$.

### Opposite category
Same as dual category: $\mathcal{C}^{op}$ with reversed morphisms.

### Power
The power $A^S$ is the product $\prod_{s \in S} A$, representing the internal hom $[S, A]$ when it exists.

### Preadditive category
A category enriched over abelian groups, i.e., each hom-set has an abelian group structure compatible with composition.

### Product
The product $\prod_{i \in I} A_i$ is the limit of the discrete diagram $\{A_i\}_{i \in I}$, with projections $\pi_j: \prod_{i \in I} A_i \to A_j$.

### Pullback
The pullback of $f: A \to C$ and $g: B \to C$ is the limit of the cospan diagram, yielding $P$ with morphisms to $A$ and $B$ making the square commute.

### Pushout
The pushout of $f: C \to A$ and $g: C \to B$ is the colimit of the span diagram.

### Reflective subcategory
A full subcategory $\mathcal{D} \hookrightarrow \mathcal{C}$ is reflective if the inclusion has a left adjoint.

### Representable functor
A functor $F: \mathcal{C}^{op} \to \mathbf{Set}$ is representable if $F \cong \text{Hom}_\mathcal{C}(-, c)$ for some $c \in \mathcal{C}$.

### Retract
An object $A$ is a retract of $B$ if there exist $i: A \to B$ and $r: B \to A$ with $r \circ i = \text{id}_A$.

### Slice category
The slice category $\mathcal{C}/c$ for $c \in \mathcal{C}$ has:
- Objects: morphisms $f: d \to c$ in $\mathcal{C}$
- Morphisms: commutative triangles

### Split exact sequence
An exact sequence $0 \to A \xrightarrow{i} B \xrightarrow{p} C \to 0$ splits if there exist $r: B \to A$ and $s: C \to B$ with $r \circ i = \text{id}_A$ and $p \circ s = \text{id}_C$.

### Split monomorphism / split epimorphism
A monomorphism $f: A \to B$ splits if there exists $g: B \to A$ with $g \circ f = \text{id}_A$. Dually for split epimorphisms.

### Subobject
A subobject of $X$ is an equivalence class of monomorphisms into $X$, where $f: A \to X$ and $g: B \to X$ are equivalent if they factor through each other.

### Terminal object
An object $1 \in \mathcal{C}$ is terminal if for every object $A$, there exists a unique morphism $A \to 1$.

### Universal arrow / universal property
A universal arrow from $c \in \mathcal{C}$ to $G: \mathcal{D} \to \mathcal{C}$ is a pair $(d, \eta: c \to G(d))$ such that for any $f: c \to G(d')$, there exists unique $\bar{f}: d \to d'$ with $G(\bar{f}) \circ \eta = f$.

### Weak limit / weak colimit
A weak limit of $F: \mathcal{J} \to \mathcal{C}$ is a cone that satisfies the existence but not uniqueness part of the universal property.

### Zero object
An object that is both initial and terminal.

### Zero morphism
In a category with zero object $0$, the zero morphism $0_{A,B}: A \to B$ is the composite $A \to 0 \to B$.

## Basic Higher Category Concepts

### ∗Complicial set
A complicial set is a simplicial set equipped with a marking on each simplex, satisfying compatibility conditions. The marked simplices typically represent "thin" or "degenerate" cells.

### Cellular set
A cellular set is a presheaf on the category $\Theta$ of finite ordinals with face and degeneracy maps, generalizing simplicial sets.

### Homotopy category
The homotopy category $\text{Ho}(\mathcal{C})$ of a category with weak equivalences $\mathcal{C}$ is the localization $\mathcal{C}[W^{-1}]$ at the weak equivalences $W$.

### n-category
An $n$-category has:
- Objects (0-cells)
- 1-morphisms between objects
- 2-morphisms between 1-morphisms
- ...
- $n$-morphisms between $(n-1)$-morphisms
- All $(k>n)$-morphisms are identities

### ∞-category
An $\infty$-category is a category enriched over $\infty$-groupoids, typically modeled as a quasi-category (Kan-complex-enriched category).

### Weak n-category
A weak $n$-category has composition and identities satisfying coherence laws only up to higher isomorphisms.

### Strict n-category
A strict $n$-category has composition strictly associative and unital at all levels.

### Bicategory
A bicategory consists of:
- Objects
- 1-morphisms between objects
- 2-morphisms between 1-morphisms
with composition associative and unital up to coherent isomorphism.

### Globular set
A globular set is a presheaf on the globular category $\mathbb{G}$ with objects $[n]$ and parallel source/target maps.

### Nerve of a category
(Already defined in Classical section)

### Quasicategory
A quasicategory is a simplicial set $X$ satisfying the inner horn lifting property: every map $\Lambda^n_i \to X$ ($0 < i < n$) extends to $\Delta^n \to X$.

### Kan complex
A Kan complex is a simplicial set satisfying all horn lifting properties: every map $\Lambda^n_i \to X$ extends to $\Delta^n \to X$ for all $0 \leq i \leq n$.

### Simplicial set
A simplicial set is a functor $X: \Delta^{op} \to \mathbf{Set}$ from the opposite of the simplex category.

### Complete Segal space
A complete Segal space is a Reedy fibrant simplicial space $X: \Delta^{op} \to \mathbf{sSet}$ satisfying:
- Segal condition: $X_n \to X_1 \times_{X_0} \cdots \times_{X_0} X_1$ is a weak equivalence
- Completeness: the map $X_0 \to X_{hoequiv}$ is a weak equivalence

### Segal category
A Segal category is a simplicial space satisfying the Segal condition with discrete space of objects $X_0$.

### Homotopy hypothesis
The homotopy hypothesis asserts that $n$-groupoids model homotopy $n$-types, with $\infty$-groupoids modeling all homotopy types.

## Types of Higher Categories

### Cartesian closed category
A category $\mathcal{C}$ with finite products such that for each object $A$, the functor $(-) \times A$ has a right adjoint $[A, -]$.

### Closed category
A symmetric monoidal category where each functor $(-) \otimes A$ has a right adjoint $[A, -]$.

### Compact closed category
A symmetric monoidal category where every object $A$ has a dual $A^*$ with evaluation and coevaluation satisfying the triangle identities.

### Double category
A double category has:
- Objects
- Horizontal and vertical 1-morphisms
- 2-cells with both horizontal and vertical composition

### Enriched category
A $\mathcal{V}$-enriched category has hom-objects $\mathcal{C}(A,B) \in \mathcal{V}$ with composition and identities as morphisms in $\mathcal{V}$.

### Internal category
An internal category in $\mathcal{E}$ consists of objects $C_0, C_1 \in \mathcal{E}$ with structure maps (source, target, identity, composition) satisfying category axioms internally.

### Monoidal category
A category $\mathcal{C}$ with:
- Tensor product $\otimes: \mathcal{C} \times \mathcal{C} \to \mathcal{C}$
- Unit object $I$
- Associativity and unit isomorphisms satisfying coherence conditions

### Braided monoidal category
A monoidal category with braiding isomorphism $\beta_{A,B}: A \otimes B \cong B \otimes A$ satisfying the hexagon identities.

### Monoidal ∞-category
An $\infty$-category $\mathcal{C}^\otimes \to N(\mathrm{Fin}_*)$ over the nerve of pointed finite sets, encoding a coherent monoidal structure.

### Omega-category (ω-category)
An $\omega$-category has cells of all dimensions $n \geq 0$ with source, target, identity, and composition operations satisfying strict associativity and interchange laws.

### Pivotal category
A monoidal category with chosen isomorphisms $A \cong A^{**}$ compatible with the monoidal structure.

### Fusion category
A semisimple rigid monoidal category with finitely many simple objects and finite-dimensional hom-spaces.

### Modular tensor category
A ribbon fusion category with non-degenerate braiding (the $S$-matrix is invertible).

### Symmetric monoidal category
A braided monoidal category where $\beta_{B,A} \circ \beta_{A,B} = \text{id}_{A \otimes B}$.

### Virtual double category
A double category where horizontal composition is only partially defined, subject to coherence conditions.

## Morphisms & Cells

### k-morphism
In an $n$-category, a $k$-morphism is a morphism between $(k-1)$-morphisms for $1 \leq k \leq n$.

### 2-morphism
A morphism between 1-morphisms in a 2-category or bicategory.

### Higher morphism
Any $k$-morphism for $k > 1$ in a higher category.

### Globular k-cell
A $k$-dimensional cell in a globular set with source and target $(k-1)$-cells.

### Icon
A 2-morphism in a double category filling a square of 1-morphisms.

### Lax natural transformation
For 2-functors $F, G: \mathcal{C} \to \mathcal{D}$, a lax natural transformation has components $\alpha_c: F(c) \to G(c)$ and 2-cells $\alpha_f: G(f) \circ \alpha_c \Rightarrow \alpha_{c'} \circ F(f)$ satisfying coherence.

### Oplax natural transformation
Dual to lax: 2-cells go $\alpha_f: \alpha_{c'} \circ F(f) \Rightarrow G(f) \circ \alpha_c$.

### Pseudonatural transformation
A lax natural transformation where all 2-cells $\alpha_f$ are isomorphisms.

### Modification
A modification between natural transformations $\alpha, \beta: F \Rightarrow G$ assigns to each object $c$ a 2-morphism $\Gamma_c: \alpha_c \Rightarrow \beta_c$ satisfying naturality.

### Equivalence in higher categories
A morphism with a quasi-inverse up to coherent higher isomorphisms. In an $(\infty,1)$-category, an equivalence is a morphism that becomes an isomorphism in the homotopy category.

### Adjoint equivalence
An equivalence realized by an adjunction where unit and counit are isomorphisms.

## Functors & Transformations

### ∞-functor
A map of simplicial sets $F: \mathcal{C} \to \mathcal{D}$ between quasi-categories preserving composition up to homotopy.

### Functor between bicategories
A (pseudo)functor $F: \mathcal{B} \to \mathcal{B}'$ preserving composition and identities up to coherent 2-isomorphism.

### Homotopy coherent diagram
A functor from a simplicial category to an $\infty$-category, encoding coherent homotopies between composites.

### Lax functor
A functor between bicategories with coherence 2-cells $F(g \circ f) \Rightarrow F(g) \circ F(f)$ and $1_{F(A)} \Rightarrow F(1_A)$.

### Oplax functor
Dual: coherence 2-cells $F(g) \circ F(f) \Rightarrow F(g \circ f)$ and $F(1_A) \Rightarrow 1_{F(A)}$.

### Pseudofunctor
A lax functor where all coherence 2-cells are isomorphisms.

### Transformation between ∞-functors
A homotopy between maps of quasi-categories, represented by a map $\mathcal{C} \times \Delta^1 \to \mathcal{D}$.

### Natural isomorphism up to higher equivalence
In an $n$-category, a natural transformation whose components are equivalences.

## Limits & Colimits

### Homotopy colimit
The derived functor of the colimit functor, computed by replacing the diagram with a cofibrant resolution.

### Homotopy limit
The derived functor of the limit functor, computed using fibrant resolutions.

### ∞-categorical colimit
A colimit in an $\infty$-category, representing the initial object of the $\infty$-category of cocones.

### ∞-categorical limit
Dual: the terminal object in the $\infty$-category of cones.

### Weighted limit
The limit of $J: \mathcal{C} \to \mathcal{D}$ weighted by $W: \mathcal{C}^{op} \to \mathbf{Set}$ is the representation of the functor $d \mapsto [\mathcal{C}, \mathbf{Set}](W, \mathcal{D}(d, J-))$.

### Bicolimit
A 2-categorical colimit, defined up to equivalence rather than isomorphism.

### Flexible limit
A limit in a 2-category where the universal property holds up to isomorphism rather than equality.

### Kan extension in higher categories
The $\infty$-categorical generalization where the universal property holds up to contractible space of choices.

### Lax limit
A weak 2-limit where the universal property provides existence but not uniqueness.

### Pseudolimit
A 2-limit where factorizations are unique up to unique isomorphism.

### End
(Already defined in Classical section)

### Bilimit
A 2-categorical limit, dual to bicolimit.

## Adjunctions & Duality

### Adjunction in bicategories
1-morphisms $L: A \to B$ and $R: B \to A$ with 2-morphisms $\eta: 1_A \Rightarrow R \circ L$ and $\epsilon: L \circ R \Rightarrow 1_B$ satisfying triangle identities up to coherent modification.

### Biadjunction
An adjunction in a bicategory where the triangle identities hold up to invertible modifications.

### Lax adjunction
An adjunction where one or both triangle identities hold only laxly.

### ∞-adjunction
An adjunction in an $\infty$-category, characterized by the mapping spaces $\text{Map}(L(x), y) \simeq \text{Map}(x, R(y))$ being equivalent.

### Coend calculus
The calculus of coends, using the universal property to manipulate expressions involving $\int^c F(c,c)$.

### Dualizable object
In a monoidal category, an object $A$ with dual $A^*$ and evaluation/coevaluation maps satisfying the triangle identities.

### Fully dualizable object
In a monoidal $n$-category, an object with duals at all levels up to dimension $n$.

### Serre duality
In a triangulated category, a contravariant equivalence $D: \mathcal{C}^{op} \to \mathcal{C}$ with natural isomorphisms $\text{Hom}(X,Y) \cong \text{Hom}(Y,DX)^*$.

### Verdier duality
The duality on the derived category of sheaves given by $\mathbb{D}(F) = R\mathcal{H}om(F, \omega_X)$ for dualizing complex $\omega_X$.

### Grothendieck duality
For proper morphism $f: X \to Y$, the isomorphism $Rf_* R\mathcal{H}om(F, f^!\mathcal{O}_Y) \cong R\mathcal{H}om(Rf_*F, \mathcal{O}_Y)$.

## Monads & Algebras

### Monad in a bicategory
An endomorphism $T: A \to A$ with 2-morphisms $\mu: T \circ T \Rightarrow T$ and $\eta: 1_A \Rightarrow T$ satisfying associativity and unit laws.

### Comonad
Dual: an endomorphism with comultiplication $\delta: T \Rightarrow T \circ T$ and counit $\epsilon: T \Rightarrow 1_A$.

### Eilenberg–Moore object
The object of algebras for a monad, when it exists in the ambient bicategory.

### Kleisli object
The free algebras for a monad, representing the initial way to resolve the monad.

### Distributive law
A 2-morphism $\lambda: S \circ T \Rightarrow T \circ S$ between monads satisfying compatibility with their structures.

### Algebras for a monad
An algebra for monad $(T, \mu, \eta)$ is an object $A$ with structure map $\alpha: T(A) \to A$ satisfying $\alpha \circ \mu_A = \alpha \circ T(\alpha)$ and $\alpha \circ \eta_A = \text{id}_A$.

### Coalgebras
Dual: an object $C$ with $\gamma: C \to T(C)$ satisfying coassociativity and counit conditions.

### Monadic functor
A functor $U: \mathcal{B} \to \mathcal{A}$ that has a left adjoint and exhibits $\mathcal{B}$ as equivalent to the category of algebras for the induced monad.

### Barr–Beck theorem
$U: \mathcal{B} \to \mathcal{A}$ is monadic if and only if:
- $U$ has a left adjoint
- $U$ reflects isomorphisms
- $\mathcal{B}$ has coequalizers of $U$-split pairs and $U$ preserves them

### Lax algebra
For a 2-monad $T$, a lax algebra has structure 2-morphism $\alpha: T(A) \to A$ satisfying laws up to coherent 2-cells.

### Pseudo-monad
A monad in a bicategory where associativity and unit laws hold up to coherent isomorphism.

### Pseudo-algebra
An algebra for a pseudo-monad where the algebra laws hold up to coherent isomorphism.

## Operads & Algebraic Structures

### Operad
An operad $\mathcal{P}$ consists of:
- Objects $\mathcal{P}(n)$ of $n$-ary operations for each $n \geq 0$
- Composition maps $\gamma: \mathcal{P}(k) \times \mathcal{P}(n_1) \times \cdots \times \mathcal{P}(n_k) \to \mathcal{P}(n_1 + \cdots + n_k)$
- Unit $1 \in \mathcal{P}(1)$
- $\Sigma_n$-action on $\mathcal{P}(n)$
satisfying associativity, unit, and equivariance axioms.

### Multicategory
(Already defined in Classical section)

### PROP
A PROP (product and permutation category) is a symmetric monoidal category whose objects are natural numbers with monoidal product given by addition.

### Lawvere theory
(Already defined in Classical section)

### Topological operad
An operad enriched in topological spaces, with continuous composition maps.

### Symmetric operad
An operad in the category of $\mathbb{S}$-modules, where $\mathbb{S}$ is the groupoid of finite sets and bijections.

### Cyclic operad
An operad with additional $S_{n+1}$-action on $\mathcal{P}(n)$ compatible with composition, encoding operations with no distinguished output.

### Modular operad
An operad with operations labeled by genus and allowing self-gluings, used in the study of moduli spaces of curves.

### Algebra over an operad
For an operad $\mathcal{P}$, a $\mathcal{P}$-algebra is an object $A$ with structure maps $\mathcal{P}(n) \otimes A^{\otimes n} \to A$ satisfying associativity and unit conditions.

### Coalgebra over an operad
Dual: structure maps $C \to \mathcal{P}(n) \otimes C^{\otimes n}$ satisfying coassociativity.

### ∞-operad
A fibration $\mathcal{O}^\otimes \to N(\mathrm{Fin}_*)$ of simplicial sets satisfying Segal conditions, encoding coherent operadic composition.

### Dendroidal set
A presheaf on the category $\Omega$ of trees, generalizing simplicial sets to encode operadic structures.

### Colored operad
An operad with multiple sorts, having operations $\mathcal{P}(c_1,\ldots,c_n;c)$ with typed inputs and output.

### Properad
A generalization of operads allowing operations with multiple inputs and outputs, encoded as directed graphs.

### ∞-properad
The $\infty$-categorical version, typically modeled using presheaves on graphs with appropriate Segal conditions.

## Topology & Homotopy Theory

### Classifying space
For a group $G$, the classifying space $BG$ has $\pi_1(BG) = G$ and contractible universal cover $EG$.

### Delooping
For a pointed space $X$, a delooping is a space $BX$ with $\Omega BX \simeq X$.

### Loop space
The space $\Omega X = \text{Map}_*((S^1,*),(X,*))$ of based loops in $X$.

### Loop space object
In an $\infty$-category, the pullback of $* \to X \leftarrow *$.

### Mapping space
In an $\infty$-category $\mathcal{C}$, the space $\text{Map}_\mathcal{C}(X,Y)$ of morphisms from $X$ to $Y$.

### Fundamental ∞-groupoid
The $\infty$-groupoid $\Pi_\infty(X)$ with points as objects and paths up to higher homotopies as morphisms.

### Homotopy fiber
For $f: X \to Y$, the homotopy fiber over $y \in Y$ is the pullback of $f$ along $y: * \to Y$ in the $\infty$-category of spaces.

### Homotopy n-type
A space $X$ with $\pi_k(X) = 0$ for all $k > n$.

### Homotopy quotient
For $G$ acting on $X$, the homotopy quotient is $X \times_G EG = (X \times EG)/G$.

### Stabilization
The process of passing from pointed spaces to spectra by iterating the loop-suspension adjunction.

### Suspension
The suspension $\Sigma X = X \wedge S^1$ with adjunction $[\Sigma X, Y] \cong [X, \Omega Y]$.

## Model Structures

### Model category
A category $\mathcal{C}$ with three distinguished classes of morphisms:
- Weak equivalences $W$
- Fibrations $F$
- Cofibrations $C$
satisfying axioms including: existence of limits/colimits, 2-out-of-3, retracts, lifting, and factorization.

### Simplicial model category
A model category enriched over simplicial sets compatibly with the model structure.

### Quillen adjunction
An adjunction $L: \mathcal{C} \rightleftarrows \mathcal{D} : R$ where $L$ preserves cofibrations and acyclic cofibrations (equivalently, $R$ preserves fibrations and acyclic fibrations).

### Quillen equivalence
A Quillen adjunction inducing an equivalence of homotopy categories $\text{Ho}(\mathcal{C}) \simeq \text{Ho}(\mathcal{D})$.

### Fibration in model categories
A morphism in the class $F$, characterized by the right lifting property against acyclic cofibrations.

### Cofibration
A morphism in the class $C$, characterized by the left lifting property against acyclic fibrations.

### Weak equivalence
A morphism in the class $W$, becoming an isomorphism in the homotopy category.

### Left Bousfield localization
For a model category $\mathcal{C}$ and set $S$ of morphisms, the left Bousfield localization has:
- Same cofibrations
- Weak equivalences = $S$-local equivalences
- Fibrations determined by lifting

### Right Bousfield localization
Dual: keeps the same fibrations and localizes the weak equivalences.

### Monoidal model category
A model category with monoidal structure such that:
- Tensor product of cofibrations is a cofibration
- Pushout-product axiom holds

### Enriched model category
A model category enriched over a monoidal model category $\mathcal{V}$ with compatible enriched lifting properties.

### Relative category
A category $\mathcal{C}$ with a distinguished class $W$ of weak equivalences.

## Advanced Constructions

### Yoneda embedding for ∞-categories
The fully faithful functor $\mathcal{C} \to \text{Fun}(\mathcal{C}^{op}, \mathcal{S})$ into presheaves of spaces.

### Grothendieck construction
For $F: \mathcal{C} \to \mathbf{Cat}$, the category $\int F$ with objects $(c, x \in F(c))$ and morphisms respecting the functoriality.

### Straightening and unstraightening
The equivalence between fibrations $\mathcal{E} \to \mathcal{C}$ and functors $\mathcal{C} \to \mathbf{Cat}$ (or their $\infty$-categorical versions).

### Factorization system
(Already defined in Classical section)

### Orthogonal factorization system
A factorization system $(\mathcal{E}, \mathcal{M})$ where $\mathcal{E}$ and $\mathcal{M}$ are characterized by mutual orthogonality (unique lifting).

### Reflective subcategory
(Already defined in Classical section)

### Coreflective subcategory
(Already defined in Classical section)

### Exact ∞-category
An $\infty$-category with a notion of exact sequences, typically a stable $\infty$-category with a t-structure.

### Stable ∞-category
An $\infty$-category where:
- Finite limits and colimits exist
- Initial and terminal objects coincide
- Squares are pullbacks iff they are pushouts

### Presentable ∞-category
An $\infty$-category equivalent to the localization of a presheaf $\infty$-category at a small set of morphisms.

### Accessible ∞-category
An $\infty$-category with $\kappa$-compact objects generating under $\kappa$-filtered colimits.

### Topos
A category equivalent to the category of sheaves on some site, characterized by having finite limits, exponentials, and subobject classifier.

### Higher topos
An $\infty$-category satisfying the $\infty$-categorical version of Giraud's axioms.

### (∞,1)-topos
An $\infty$-topos where all $n$-morphisms for $n > 1$ are invertible.

### (∞,n)-category
An $\infty$-category where all $k$-morphisms for $k > n$ are invertible.

### Cobordism hypothesis
The statement that the $(\infty,n)$-category of fully dualizable objects in a symmetric monoidal $(\infty,n)$-category $\mathcal{C}$ is equivalent to $\text{Bord}_n$ evaluated at $\mathcal{C}$.

### Day convolution
For functors $F, G: \mathcal{C} \to \mathcal{V}$ where $\mathcal{C}$ is monoidal, the Day convolution is:
$$F \star G = \int^{c,d \in \mathcal{C}} F(c) \otimes G(d) \otimes \mathcal{C}(-, c \otimes d)$$

### Tannaka duality
The reconstruction of a group (or Hopf algebra) from its category of representations with forgetful functor.

### Twisted arrow category
The category $\text{Tw}(\mathcal{C})$ with objects being morphisms of $\mathcal{C}$ and morphisms $(f: a \to b) \to (g: c \to d)$ being commutative squares.

## Dimensional Enhancements

### 2-category
A category enriched over $\mathbf{Cat}$, having objects, 1-morphisms, and 2-morphisms with strict composition.

### 3-category
A category with objects, 1-morphisms, 2-morphisms, and 3-morphisms, with composition strict at all levels.

### n-fold category
An $n$-fold category has $n$ different directions of morphisms, generalizing double categories.

### Iterated span category
The $n$-fold category $\text{Span}_n(\mathcal{C})$ with $n$ levels of spans in $\mathcal{C}$.

### Gray-category
A category enriched over Gray's tensor product of 2-categories, giving a semi-strict 3-category.

### Trimble n-category
An iterative definition where an $n$-category is a category enriched over $(n-1)$-categories with appropriate coherence.

### Tamsamani n-category
A simplicial object in $(n-1)$-categories satisfying the Segal condition at each level.

### Street nerve
The nerve construction taking a bicategory to a simplicial category encoding its structure.

### Θ-space
A presheaf on Joyal's category $\Theta$ satisfying Segal conditions, modeling $(\infty,n)$-categories.

### Rezk completion
The fibrant replacement in the complete Segal space model structure, forcing essential surjectivity.

### Homotopy coherent nerve
The nerve functor from simplicial categories to simplicial sets, preserving the homotopy theory.

### ω-category
(Already defined in Types of Higher Categories)

## Algebraic Geometry & Physics

### Derived stack
An $\infty$-functor $\mathcal{X}: \text{CAlg}^{op} \to \mathcal{S}$ from commutative algebras to spaces, satisfying descent for étale covers.

### Higher stack
An $n$-stack is a presheaf of $(n-1)$-groupoids satisfying descent.

### Perfect stack
A derived stack whose cotangent complex has perfect amplitude in a specified range.

### Geometric Langlands program
The correspondence between $D$-modules on $\text{Bun}_G$ and quasi-coherent sheaves on $\text{Loc}_{G^\vee}$.

### Topological field theory
A symmetric monoidal functor $Z: \text{Bord}_n \to \mathcal{C}$ from the bordism category.

### Extended TQFT
A functor from the $(\infty,n)$-category of bordisms to some target $(\infty,n)$-category.

### Conformal field theory
A representation of the conformal algebra (Virasoro or current algebra) with specified properties.

### Factorization algebra
A cosheaf-like structure $\mathcal{F}: \text{Open}(M) \to \mathcal{C}$ satisfying factorization axioms for disjoint unions.

### Chiral algebra
A vertex algebra or factorization algebra on a curve, central to 2d CFT.

### Vertex operator algebra
An algebra $V$ with a state-field correspondence $Y: V \to \text{End}(V)[[z,z^{-1}]]$ satisfying locality and other axioms.

### Deformation quantization
A formal deformation of the commutative algebra of functions to a noncommutative star product.

### Drinfeld center
For a monoidal category $\mathcal{C}$, the center $Z(\mathcal{C})$ has objects $(A, \gamma)$ where $\gamma_X: A \otimes X \cong X \otimes A$ satisfies coherence.

### Hochschild cohomology
For an algebra $A$, the cohomology $HH^*(A) = \text{Ext}_{A^e}^*(A,A)$ where $A^e = A \otimes A^{op}$.

### Cyclic homology
The homology of the cyclic complex, related to Hochschild homology by the Connes' long exact sequence.

### A∞-algebra
An algebra with operations $m_n: A^{\otimes n} \to A$ satisfying the $A_\infty$ relations:
$$\sum_{i+j+k=n} (-1)^{i+jk} m_{i+1+k}(\text{id}^{\otimes i} \otimes m_j \otimes \text{id}^{\otimes k}) = 0$$

### A∞-category
A category enriched over chain complexes with higher composition operations satisfying $A_\infty$ coherence.

### L∞-algebra
A graded vector space with brackets $\ell_n: \wedge^n L \to L$ satisfying generalized Jacobi identities.

### dg-category
A category enriched over chain complexes with differential satisfying the Leibniz rule.

### Spectral category
A category enriched over spectra, the stable version of simplicial categories.

### Shifted symplectic structure
A closed 2-form of degree $n$ on a derived stack inducing a non-degenerate pairing on the tangent complex.

### Factorization homology
For a factorization algebra $\mathcal{F}$ on $M$, the factorization homology $\int_M \mathcal{F}$ is the colimit over the Ran space.