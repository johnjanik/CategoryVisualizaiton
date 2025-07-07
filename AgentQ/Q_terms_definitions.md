
---

## ✅ CLASSICAL CATEGORY THEORY

### Abelian category
An **Abelian category** is a category that has:
- A zero object,
- All binary products and coproducts,
- All kernels and cokernels,
- Every monomorphism is a kernel of some morphism, and every epimorphism is a cokernel of some morphism.

This structure allows one to perform diagram chasing as in homological algebra.

---

### Additive category
An **Additive category** is a preadditive category (i.e., enriched over the category **Ab** of abelian groups) that has all finite biproducts (products which are also coproducts).

---

### Adjoint functor theorem
The **Adjoint Functor Theorem** gives conditions under which a functor $ F : \mathcal{C} \to \mathcal{D} $ has a left adjoint. In particular, if $\mathcal{C}$ is complete, locally small, and $F$ preserves limits and satisfies the solution set condition, then $F$ has a left adjoint.

---

### Adjunction (unit, counit; left and right adjoints)
An **adjunction** between two categories $\mathcal{C}$ and $\mathcal{D}$ consists of:
- Functors $F: \mathcal{C} \to \mathcal{D}$, $G: \mathcal{D} \to \mathcal{C}$,
- Natural transformations:
  - Unit: $\eta : \text{id}_{\mathcal{C}} \Rightarrow G \circ F$,
  - Counit: $\varepsilon : F \circ G \Rightarrow \text{id}_{\mathcal{D}}$,
- Satisfying the triangle identities:
  $$
  F \xrightarrow{F\eta} FGF \xrightarrow{\varepsilon F} F = \text{id}_F,\quad G \xrightarrow{\eta G} GFG \xrightarrow{G\varepsilon} G = \text{id}_G.
  $$

Then $F$ is left adjoint to $G$, and $G$ is right adjoint to $F$.

---

### Automorphism
An **automorphism** is an isomorphism from an object to itself in a category.

---

### Balanced category
A **balanced category** is one in which every bimorphism (a morphism that is both monic and epic) is an isomorphism.

---

### Category (small, large, locally small)
A **category** $\mathcal{C}$ consists of:
- A collection of objects $\text{Ob}(\mathcal{C})$,
- For each pair $X,Y \in \text{Ob}(\mathcal{C})$, a set (or class) $\mathcal{C}(X,Y)$ of morphisms,
- Identity morphisms and associative composition satisfying identity and associativity laws.

It is **small** if both $\text{Ob}(\mathcal{C})$ and all $\mathcal{C}(X,Y)$ are sets; **large** otherwise; **locally small** if all hom-classes are sets.

---

### Category of elements
Given a presheaf $F : \mathcal{C}^{\text{op}} \to \mathbf{Set}$, its **category of elements**, denoted $\int F$, has:
- Objects: pairs $(c, x)$ where $c \in \mathcal{C}$ and $x \in F(c)$,
- Morphisms: $f : (c,x) \to (d,y)$ given by morphisms $f : c \to d$ in $\mathcal{C}$ such that $F(f)(y) = x$.

---

### Cauchy (Karoubi) completion
The **Cauchy completion** (or **Karoubi envelope**) of a category $\mathcal{C}$ is the universal category obtained by formally splitting all idempotents in $\mathcal{C}$, i.e., adding images for all idempotent morphisms $e : X \to X$ with $e^2 = e$.

---

### Comma category
Given functors $F : \mathcal{A} \to \mathcal{C}$, $G : \mathcal{B} \to \mathcal{C}$, the **comma category** $(F \downarrow G)$ has:
- Objects: triples $(a,b,f)$ where $a \in \mathcal{A}, b \in \mathcal{B}, f : F(a) \to G(b)$,
- Morphisms: $(a,b,f) \to (a',b',f')$ given by morphisms $g : a \to a'$, $h : b \to b'$ such that $G(h) \circ f = f' \circ F(g)$.

---

### Composition (associativity, identity laws)
In a category, composition of morphisms satisfies:
- Associativity: $f \circ (g \circ h) = (f \circ g) \circ h$,
- Identity: for each object $X$, there exists $\text{id}_X$ such that $f \circ \text{id}_X = f$ and $\text{id}_X \circ g = g$ whenever defined.

---

### Contravariant functor
A **contravariant functor** $F : \mathcal{C} \to \mathcal{D}$ is a mapping reversing direction of morphisms:
- $F(f \circ g) = F(g) \circ F(f)$,
- $F(\text{id}_X) = \text{id}_{F(X)}$.

Equivalently, it is a covariant functor $\mathcal{C}^{\text{op}} \to \mathcal{D}$.

---

### Copower (tensoring with a set or object)
For a category $\mathcal{C}$ tensored over $\mathbf{Set}$, the **copower** of an object $X \in \mathcal{C}$ by a set $S$ is an object $S \cdot X$ representing the functor $\mathcal{C}(X,-)^S$.

---

### Copresheaf
A **copresheaf** on a category $\mathcal{C}$ is a covariant functor $F : \mathcal{C} \to \mathbf{Set}$.

---

### Coproduct
The **coproduct** of a family of objects $\{X_i\}_{i \in I}$ in a category is an object $X = \coprod_{i \in I} X_i$ equipped with morphisms $\iota_i : X_i \to X$ such that any cocone factors uniquely through $X$.

---

### Cosegment
A **cosegment** in a category is an object $I$ together with two maps $0,1 : * \rightrightarrows I$, where $*$ is terminal, such that for any object $X$, the induced map $X^I \to X \times X$ is a weak equivalence (in a model-categorical context).

---

### Coslice category
Given an object $A$ in $\mathcal{C}$, the **coslice category** $A/\mathcal{C}$ has:
- Objects: morphisms $f : A \to X$ in $\mathcal{C}$,
- Morphisms: $f \to g$ given by $h : X \to Y$ such that $h \circ f = g$.

---

### Coequalizer
The **coequalizer** of a pair of morphisms $f,g : X \rightrightarrows Y$ is a morphism $q : Y \to Z$ such that $q \circ f = q \circ g$, and is universal with this property.

---

### Coefficient (in enriched/hyperdoctrine contexts)
In enriched category theory or hyperdoctrines, a **coefficient** is typically an object in a base category used for enrichment or indexing logical predicates.

---

### Coend
The **coend** of a bifunctor $F : \mathcal{C}^{\text{op}} \times \mathcal{C} \to \mathcal{D}$ is the coequalizer of the diagram:
$$
\coprod_{f : c \to c'} F(c',c) \rightrightarrows \coprod_c F(c,c),
$$
denoted $\int^{c \in \mathcal{C}} F(c,c)$.

---

### Coreflective subcategory
A **coreflective subcategory** $\mathcal{D} \subseteq \mathcal{C}$ is one for which the inclusion functor has a right adjoint (called the coreflector).

---

### Covariant functor
A **covariant functor** $F : \mathcal{C} \to \mathcal{D}$ preserves composition and identities:
- $F(f \circ g) = F(f) \circ F(g)$,
- $F(\text{id}_X) = \text{id}_{F(X)}$.

---

### Dinatural transformation
A **dinatural transformation** $\alpha : F \ddot{\Rightarrow} G$ between functors $F,G : \mathcal{C}^{\text{op}} \times \mathcal{C} \to \mathcal{D}$ satisfies a coherence condition involving both variables.

---

### Dual category (opposite category)
The **dual category** or **opposite category** $\mathcal{C}^{\text{op}}$ has the same objects as $\mathcal{C}$, but reversed morphisms: $\mathcal{C}^{\text{op}}(X,Y) = \mathcal{C}(Y,X)$.

---

### End
The **end** of a bifunctor $F : \mathcal{C}^{\text{op}} \times \mathcal{C} \to \mathcal{D}$ is the equalizer of the diagram:
$$
\prod_c F(c,c) \rightrightarrows \prod_{f : c \to c'} F(c,c'),
$$
denoted $\int_{c \in \mathcal{C}} F(c,c)$.

---

### Equalizer
The **equalizer** of a pair of morphisms $f,g : X \rightrightarrows Y$ is a morphism $e : E \to X$ such that $f \circ e = g \circ e$, and is universal with this property.

---

### Essentially surjective functor
A functor $F : \mathcal{C} \to \mathcal{D}$ is **essentially surjective** if for every object $D$ in $\mathcal{D}$, there exists an object $C$ in $\mathcal{C}$ such that $F(C) \cong D$.

---

### Exact category
An **exact category** is an additive category equipped with a distinguished class of short exact sequences (called conflations), satisfying axioms generalizing those of abelian categories.

---

### Factorization system (Epi–Mono, etc.)
A **factorization system** $(\mathcal{E}, \mathcal{M})$ on a category $\mathcal{C}$ consists of two classes of morphisms such that:
- Every morphism factors as an $\mathcal{E}$-map followed by an $\mathcal{M}$-map,
- $\mathcal{E}$ and $\mathcal{M}$ are orthogonal.

Example: (epi, mono) in **Set**.

---

### Fully faithful functor
A **fully faithful functor** $F : \mathcal{C} \to \mathcal{D}$ induces bijections on hom-sets: $F_{X,Y} : \mathcal{C}(X,Y) \to \mathcal{D}(F(X),F(Y))$.

---

### Functor (covariant, contravariant)
A **functor** $F : \mathcal{C} \to \mathcal{D}$ is a mapping preserving composition and identities. If it reverses morphism directions, it is **contravariant**; otherwise, **covariant**.

---

### Functor category
The **functor category** $[\mathcal{C}, \mathcal{D}]$ has:
- Objects: functors $F : \mathcal{C} \to \mathcal{D}$,
- Morphisms: natural transformations between them.

---

### Full functor
A **full functor** $F : \mathcal{C} \to \mathcal{D}$ induces surjections on hom-sets.

---

### Grothendieck fibration
A **Grothendieck fibration** $p : \mathcal{E} \to \mathcal{B}$ is a functor such that for every morphism $f : b \to p(e)$ in $\mathcal{B}$, there exists a Cartesian lift in $\mathcal{E}$.

---

### Grothendieck topology
A **Grothendieck topology** on a category $\mathcal{C}$ is a collection of sieves called covering families, satisfying certain axioms that allow one to define sheaves on $\mathcal{C}$.

---

### Image (regular image, categorical image)
The **image** of a morphism $f : X \to Y$ is the smallest subobject through which $f$ factors. In many categories, it's the equalizer of the cokernel pair of $f$.

---

### Initial object
An **initial object** $0$ in a category is one such that for every object $X$, there exists a unique morphism $0 \to X$.

---

### Isomorphism
An **isomorphism** $f : X \to Y$ is a morphism admitting an inverse $g : Y \to X$ such that $f \circ g = \text{id}_Y$, $g \circ f = \text{id}_X$.

---

### Kan extension (left and right)
Given functors $F : \mathcal{C} \to \mathcal{D}$, $K : \mathcal{C} \to \mathcal{E}$, the **right Kan extension** $\text{Ran}_K F$ is the best approximation of $F$ along $K$ via a universal cone. Similarly for **left Kan extension** $\text{Lan}_K F$.

---

### Kernel
In a category with zero morphisms, the **kernel** of a morphism $f : X \to Y$ is the equalizer of $f$ and the zero morphism.

---

### Lawvere theory
A **Lawvere theory** is a category $\mathcal{T}$ with finite products, whose objects are the natural numbers, and where each object $n$ is the product of $n$ copies of $1$. Models of $\mathcal{T}$ are functors preserving finite products.

---

### Limit (inverse limit, pullback, etc.)
A **limit** of a diagram $D : \mathcal{J} \to \mathcal{C}$ is a universal cone over $D$, consisting of an object $L$ and morphisms $\pi_j : L \to D(j)$ making all triangles commute.

Special cases: product, equalizer, pullback.

---

### Locally presentable category
A **locally presentable category** is a cocomplete category with a small set of small presentable generators.

---

### Monomorphism
A **monomorphism** $f : X \to Y$ is a morphism such that for any $g,h : Z \to X$, $f \circ g = f \circ h \implies g = h$.

---

### Multicategory
A **multicategory** generalizes a category by allowing morphisms to have multiple inputs: a morphism $f : (X_1,\dots,X_n) \to Y$.

---

### Natural transformation (vertical/horizontal composition)
A **natural transformation** $\eta : F \Rightarrow G$ between functors $F,G : \mathcal{C} \to \mathcal{D}$ assigns to each object $X$ a morphism $\eta_X : F(X) \to G(X)$ such that for each $f : X \to Y$, the naturality square commutes.

**Vertical composition**: composing components.


**Horizontal composition**: composing across functors.

---

### Natural isomorphism
A **natural isomorphism** is a natural transformation whose components are all isomorphisms.

---

### Nerve of a category
The **nerve** $N(\mathcal{C})$ of a category $\mathcal{C}$ is a simplicial set where:
- $N(\mathcal{C})_n$ is the set of composable strings of $n$ morphisms in $\mathcal{C}$,
- Face/degeneracy maps correspond to composition/insertion of identities.

---

### Opposite category
See **Dual category** above.

---

### Power (exponentials, internal homs)
In a closed monoidal category, the **power** of an object $X$ by a set $S$ is an object $X^S$ representing the functor $\mathcal{C}(S \cdot (-), X)$.

---

### Preadditive category
A **preadditive category** is a category enriched over the category **Ab** of abelian groups; i.e., hom-sets are abelian groups and composition is bilinear.

---

### Product
The **product** of a family $\{X_i\}_{i \in I}$ is an object $P$ with projections $\pi_i : P \to X_i$ such that any cone over the family factors uniquely through $P$.

---

### Pullback
The **pullback** of morphisms $f : X \to Z$, $g : Y \to Z$ is the limit of the diagram $X \xrightarrow{f} Z \xleftarrow{g} Y$, often denoted $X \times_Z Y$.

---

### Pushout
The **pushout** of morphisms $f : Z \to X$, $g : Z \to Y$ is the colimit of the diagram $X \xleftarrow{f} Z \xrightarrow{g} Y$, often denoted $X \amalg_Z Y$.

---

### Reflective subcategory
A **reflective subcategory** $\mathcal{D} \subseteq \mathcal{C}$ is one for which the inclusion has a left adjoint (the reflector).

---

### Representable functor
A **representable functor** is a functor isomorphic to $\mathcal{C}(A, -)$ for some object $A$.

---

### Retract (section/retraction)
An object $A$ is a **retract** of $B$ if there exist morphisms $s : A \to B$ (section), $r : B \to A$ (retraction) such that $r \circ s = \text{id}_A$.

---

### Slice category
Given an object $A$ in $\mathcal{C}$, the **slice category** $\mathcal{C}/A$ has:
- Objects: morphisms $f : X \to A$,
- Morphisms: $f \to g$ given by $h : X \to Y$ such that $g \circ h = f$.

---

### Split exact sequence
A **split exact sequence** is a short exact sequence $0 \to A \xrightarrow{i} B \xrightarrow{p} C \to 0$ such that there exists a section $s : C \to B$ with $p \circ s = \text{id}_C$.

---

### Split monomorphism / split epimorphism
A **split monomorphism** is a morphism with a retraction. A **split epimorphism** is a morphism with a section.

---

### Subobject (subobject classifier in a topos)
A **subobject** of an object $X$ is an isomorphism class of monomorphisms into $X$. In a topos, a **subobject classifier** is an object $\Omega$ such that subobjects of any object $X$ correspond to morphisms $X \to \Omega$.

---

### Terminal object
A **terminal object** $1$ is one such that for every object $X$, there is a unique morphism $X \to 1$.

---

### Universal arrow / universal property
A **universal arrow** from an object $X$ to a functor $F$ is a pair $(A, u : X \to F(A))$ initial among all such arrows. A **universal property** characterizes an object up to unique isomorphism via such a universal arrow.

---

### Weak limit / weak colimit
A **weak limit** is like a limit, but without requiring uniqueness of the mediating morphism.

---

### Zero object
A **zero object** is both initial and terminal.

---

### Zero morphism
In a category with zero object, the **zero morphism** $0_{X,Y} : X \to Y$ is the composite $X \to 0 \to Y$.

---

## 📐 HIGHER CATEGORY THEORY — Definitions continue in Part 2  
Let me know whether you'd like the continuation of these definitions for Higher Categories, ∞-Categories, Model Structures, etc.

Certainly! Below are the **mathematically precise definitions** for terms in the categories of **Basic Higher Category Concepts**, **Types of Higher Categories**, and **Morphisms & Cells**.

---

## ✅ BASIC HIGHER CATEGORY CONCEPTS

### ∗Complicial set  
A **complicial set** is a simplicial set equipped with a marking (distinguished subset of simplices) satisfying axioms that model the structure of an $(\infty, n)$-category. The "∗" often indicates a variation or specific type of complicial structure (e.g., with extra coherence conditions).

---

### Cellular set  
A **cellular set** is a presheaf on the category $\Theta_n$ (or $\Theta$), used to model higher categories, especially weak $\omega$-categories. It generalizes simplicial sets to higher globular dimensions.

---

### Homotopy category  
The **homotopy category** $\mathrm{Ho}(\mathcal{C})$ of a category $\mathcal{C}$ with weak equivalences is the category obtained by formally inverting the weak equivalences. For example, the homotopy category of spaces is obtained from topological spaces by inverting homotopy equivalences.

---

### n-category  
An **n-category** is a higher category where all $k$-morphisms for $k > n$ are identities (strictly or up to equivalence). This includes 1-categories (ordinary categories), 2-categories, etc.

---

### ∞-category  
An **∞-category** (also called $(\infty, 1)$-category) is a higher category where:
- All $k$-morphisms for $k \geq 2$ are invertible,
- Composition is associative and unital up to coherent higher morphisms.

Common models include quasicategories, complete Segal spaces, and simplicial categories.

---

### Weak n-category  
A **weak n-category** is an n-category where composition of higher morphisms is only associative and unital up to coherent higher isomorphisms. These generalize bicategories and tricategories to higher dimensions.

---

### Strict n-category  
A **strict n-category** is an n-category where all compositions are strictly associative and unital. It can be defined recursively: a strict 0-category is a set, and a strict $n$-category is a category enriched over strict $(n-1)$-categories.

---

### Bicategory  
A **bicategory** is a weak 2-category: it has objects, 1-morphisms (which compose associatively only up to natural isomorphism), and 2-morphisms. It satisfies coherence axioms ensuring that diagrams involving associators and unitors commute.

---

### Globular set  
A **globular set** is a presheaf on the **globe category** $\mathbb{G}$, whose objects are finite ordinals $[n]$, and morphisms encode source and target maps between cells. It provides the basic shape for defining higher categories via globular models.

---

### Nerve of a category  
(Already defined above under Classical Category Theory.)

---

### Quasicategory  
A **quasicategory** (also called a weak Kan complex) is a simplicial set satisfying the inner horn-filling condition. It models an $(\infty,1)$-category, where edges represent morphisms and higher simplices encode composites and coherence data.

---

### Kan complex  
A **Kan complex** is a simplicial set where every horn admits a filler. It models an $\infty$-groupoid — an $(\infty, 0)$-category — where all morphisms are invertible.

---

### Simplicial set  
A **simplicial set** is a presheaf on the simplex category $\Delta$. It assigns to each finite ordered set $[n] = \{0 < 1 < \dots < n\}$ a set of $n$-simplices, with face and degeneracy maps modeling simplicial shapes.

---

### Complete Segal space  
A **complete Segal space** is a simplicial space $X_\bullet$ such that:
- Each $X_n$ is a Kan complex,
- The Segal maps $X_n \to X_1 \times_{X_0} \cdots \times_{X_0} X_1$ are weak equivalences,
- The completeness condition ensures that equivalent objects are equal in $X_0$.

It models an $(\infty,1)$-category.

---

### Segal category  
A **Segal category** is a simplicial space $X_\bullet$ where:
- $X_0$ is discrete,
- The Segal maps $X_n \to X_1 \times_{X_0} \cdots \times_{X_0} X_1$ are weak equivalences.

It also models an $(\infty,1)$-category but with less structure than a complete Segal space.

---

### Homotopy hypothesis  
The **homotopy hypothesis** asserts that the $(\infty,1)$-category of spaces is equivalent to the $(\infty,1)$-category of $\infty$-groupoids. In other words, homotopy types are equivalent to weak $\infty$-groupoids.

---

## ✅ TYPES OF HIGHER CATEGORIES

### Cartesian closed category  
A **Cartesian closed category** is a category with finite products where the product functor has a right adjoint, giving an internal hom: $\mathcal{C}(A \times B, C) \cong \mathcal{C}(A, [B,C])$.

---

### Closed category  
A **closed category** is a category equipped with internal homs $[-,-]$ and a unit object, satisfying certain coherence axioms. It may not necessarily have a tensor product.

---

### Compact closed category  
A **compact closed category** is a symmetric monoidal category where every object $A$ has a dual $A^*$ such that the unit and counit satisfy zigzag identities.

---

### Double category  
A **double category** has two kinds of morphisms: horizontal and vertical, together with squares that relate them. It can be seen as a category internal to **Cat**.

---

### Enriched category  
An **enriched category** $\mathcal{C}$ over a monoidal category $(\mathcal{V}, \otimes, I)$ consists of:
- A collection of objects,
- Hom-objects $\mathcal{C}(A,B) \in \mathcal{V}$,
- Identity and composition morphisms in $\mathcal{V}$, satisfying associativity and identity laws.

---

### Internal category  
An **internal category** in a category $\mathcal{E}$ with pullbacks consists of:
- Objects of objects and morphisms in $\mathcal{E}$,
- Source, target, identity, and composition morphisms in $\mathcal{E}$,
- Satisfying the usual category axioms expressed as commutative diagrams.

---

### Monoidal category  
A **monoidal category** is a category $\mathcal{C}$ equipped with:
- A bifunctor $\otimes : \mathcal{C} \times \mathcal{C} \to \mathcal{C}$,
- A unit object $I$,
- Associator and left/right unitors satisfying coherence conditions.

---

### Braided monoidal category  
A **braided monoidal category** is a monoidal category with a natural isomorphism $c_{A,B} : A \otimes B \to B \otimes A$ (a braiding), satisfying hexagon identities.

---

### Monoidal ∞-category  
A **monoidal ∞-category** is an ∞-category equipped with a coherently associative and unital tensor product. It can be modeled using cocartesian fibrations over $\Delta^\text{op}$, or as algebras in the ∞-category of ∞-categories.

---

### Omega-category (ω-category)  
An **ω-category** (or **infinity-category**) is a strict ∞-category where all $k$-morphisms exist for $k \geq 0$, with strict composition in all dimensions.

---

### Pivotal category  
A **pivotal category** is a rigid monoidal category where each object is equipped with a canonical isomorphism between its double dual and itself.

---

### Fusion category  
A **fusion category** is a semisimple rigid monoidal category with finitely many simple objects, finite-dimensional hom-spaces, and a simple unit object.

---

### Modular tensor category  
A **modular tensor category** is a ribbon fusion category whose $S$-matrix (defined via traces of braidings) is non-degenerate. It plays a central role in conformal field theory and topological quantum computing.

---

### Symmetric monoidal category  
A **symmetric monoidal category** is a braided monoidal category where the braiding satisfies $c_{B,A} \circ c_{A,B} = \text{id}_{A \otimes B}$.

---

## ✅ MORPHISMS & CELLS

### k-morphism  
In an $n$-category or $\infty$-category, a **k-morphism** is a morphism at level $k$, with $k \leq n$ (or unbounded in the case of $\omega$-categories). For example:
- 0-morphisms: objects,
- 1-morphisms: ordinary arrows,
- 2-morphisms: transformations between functors, etc.

---

### 2-morphism  
In a 2-category or bicategory, a **2-morphism** is a morphism between 1-morphisms. It can be composed vertically and horizontally.

---

### Higher morphism  
A **higher morphism** refers to any $k$-morphism for $k \geq 2$ in a higher categorical context.

---

### Globular k-cell  
A **globular k-cell** is a morphism in a globular higher category, represented as a directed edge between $k-1$-cells. It is part of the globular shape used in definitions of strict and weak ω-categories.

---

### Icon  
An **icon** is a special kind of 2-cell between lax functors of bicategories, which is trivial on objects and satisfies additional naturality conditions.

---

### Lax natural transformation  
A **lax natural transformation** $\alpha : F \Rightarrow G$ between 2-functors $F,G : \mathcal{C} \to \mathcal{D}$ consists of:
- Components $\alpha_X : F(X) \to G(X)$,
- Natural 2-cells $\alpha_f : G(f) \circ \alpha_X \Rightarrow \alpha_Y \circ F(f)$,
- Not required to be invertible.

---

### Oplax natural transformation  
An **oplax natural transformation** is like a lax one, but with the direction of the 2-cells reversed: $\alpha_f : \alpha_Y \circ F(f) \Rightarrow G(f) \circ \alpha_X$.

---

### Pseudonatural transformation  
A **pseudonatural transformation** is a lax or oplax natural transformation where all the 2-cells $\alpha_f$ are invertible.

---

### Modification  
A **modification** is a 3-cell between pseudonatural transformations. Given pseudonatural transformations $\alpha, \beta : F \Rightarrow G$, a modification $\Gamma : \alpha \Rrightarrow \beta$ assigns to each object $X$ a 2-cell $\Gamma_X : \alpha_X \Rightarrow \beta_X$, satisfying coherence conditions.

---

### Equivalence in higher categories  
An **equivalence** in a higher category is a morphism $f : X \to Y$ for which there exists $g : Y \to X$ and invertible 2-cells $f \circ g \Rightarrow \text{id}_Y$, $g \circ f \Rightarrow \text{id}_X$.

---

### Adjoint equivalence  
An **adjoint equivalence** is an equivalence $(f,g,\eta,\varepsilon)$ where the unit and counit satisfy the triangle identities, making it an adjunction whose unit and counit are invertible.


---

## ✅ FUNCTORS & TRANSFORMATIONS

### ∞-functor  
An **∞-functor** $F : \mathcal{C} \to \mathcal{D}$ between ∞-categories is a map of simplicial sets (if working with quasicategories) that preserves the categorical structure, including composition and identities up to coherent higher morphisms.

---

### Functor between bicategories  
A **functor between bicategories** $F : \mathcal{B} \to \mathcal{C}$ consists of:
- A mapping on objects,
- Functors $F_{A,B} : \mathcal{B}(A,B) \to \mathcal{C}(FA,FB)$,
- Natural isomorphisms expressing compatibility with composition and units (up to coherent 2-cells).

---

### Homotopy coherent diagram  
A **homotopy coherent diagram** of shape $\mathcal{C}$ in an ∞-category $\mathcal{D}$ is a simplicial functor from the simplicial category $\mathfrak{C}[\mathcal{N}\mathcal{C}]$ (the homotopy coherent nerve of $\mathcal{C}$) to $\mathcal{D}$.

---

### Lax functor  
A **lax functor** $F : \mathcal{B} \to \mathcal{C}$ between bicategories consists of:
- Object assignment,
- Functors on hom-categories,
- Natural transformations expressing lax compatibility with composition and identity,
- Not required to be invertible.

---

### Oplax functor  
An **oplax functor** is like a lax one, but the direction of the coherence natural transformations is reversed.

---

### Pseudofunctor  
A **pseudofunctor** is a lax or oplax functor where all coherence morphisms are invertible. It models a "weak" version of a 2-functor.

---

### Transformation between ∞-functors  
A **transformation between ∞-functors** $F, G : \mathcal{C} \to \mathcal{D}$ is a morphism in the ∞-category of ∞-functors $Fun(\mathcal{C}, \mathcal{D})$. In the case of quasicategories, it can be represented by a map $\Delta^1 \times \mathcal{C} \to \mathcal{D}$ satisfying certain conditions.

---

### Natural isomorphism up to higher equivalence  
A **natural isomorphism up to higher equivalence** is a transformation between ∞-functors whose components are equivalences in the target ∞-category.

---

## ✅ LIMITS & COLIMITS

### Homotopy colimit  
The **homotopy colimit** of a diagram $F : \mathcal{I} \to \mathcal{M}$ in a model category $\mathcal{M}$ is the derived version of the ordinary colimit, accounting for weak equivalences. It is defined as the left derived functor of the colimit.

---

### Homotopy limit  
The **homotopy limit** of a diagram $F : \mathcal{I} \to \mathcal{M}$ in a model category $\mathcal{M}$ is the derived version of the ordinary limit, taking into account weak equivalences. It is the right derived functor of the limit.

---

### ∞-categorical colimit  
In an ∞-category $\mathcal{C}$, the **∞-categorical colimit** of a diagram $F : \mathcal{I} \to \mathcal{C}$ is a universal cocone under $F$, expressed via a Kan extension along the inclusion of $\mathcal{I}$ into the cone category $\mathcal{I}^\triangleright$.

---

### ∞-categorical limit  
Similarly, the **∞-categorical limit** of $F : \mathcal{I} \to \mathcal{C}$ is a universal cone over $F$, defined via a Kan extension along the inclusion $\mathcal{I} \hookrightarrow \mathcal{I}^\triangleleft$.

---

### Weighted limit  
In enriched category theory, a **weighted limit** generalizes the notion of a limit by replacing cones with diagrams weighted by a functor $W : \mathcal{J} \to \mathcal{V}$, where $\mathcal{V}$ is the enriching monoidal category.

---

### Bicolimit  
A **bicolimit** in a bicategory is a colimit defined up to equivalence, rather than isomorphism. It satisfies a universal property involving pseudonatural transformations.

---

### Flexible limit  
A **flexible limit** is a type of 2-dimensional limit in a 2-category that is preserved by all 2-functors. It is a cofibrant replacement of a strict 2-limit.

---

### Kan extension in higher categories  
A **Kan extension in higher categories** generalizes the classical Kan extension to ∞-categories. Given a diagram $F : \mathcal{C} \to \mathcal{D}$ and a functor $K : \mathcal{C} \to \mathcal{E}$, the **left Kan extension** $\mathrm{Lan}_K F$ is a best approximation of $F$ along $K$ in the ∞-categorical sense.

---

### Lax limit  
A **lax limit** is a 2-dimensional limit where the universal cone commutes only up to specified 2-cells, not necessarily invertible.

---

### Pseudolimit  
A **pseudolimit** is a 2-dimensional limit where the universal cone commutes up to invertible 2-cells.

---

### End (as a limiting construction)  
(Already defined above under Classical Category Theory.)

---

### Bilimit  
A **bilimit** is a 2-dimensional limit in a bicategory that is defined up to equivalence rather than isomorphism.

---

## ✅ ADJUNCTIONS & DUALITY

### Adjunction in bicategories  
An **adjunction in a bicategory** consists of 1-morphisms $f : A \to B$, $g : B \to A$, and 2-morphisms $\eta : \text{id}_A \Rightarrow g f$, $\varepsilon : f g \Rightarrow \text{id}_B$, satisfying triangle identities up to invertible 3-cells.

---

### Biadjunction  
A **biadjunction** is an adjunction internal to a bicategory, where the unit and counit are pseudonatural transformations satisfying the triangle identities up to coherent modifications.

---

### Lax adjunction  
A **lax adjunction** is a weakening of an adjunction where the unit and counit are not invertible, and the triangle identities hold only up to further 2-cells.

---

### ∞-adjunction  
An **∞-adjunction** between ∞-functors $F : \mathcal{C} \rightleftarrows \mathcal{D} : G$ is a pair of ∞-functors together with a unit and counit transformation satisfying the triangle identities up to coherent higher equivalences.

---

### Coend calculus  
**Coend calculus** refers to techniques using coends and ends to express various constructions in category theory, such as traces, integrals, and tensor products. It plays a key role in enriched and higher category theory.

---

### Dualizable object  
An object $X$ in a monoidal category is **dualizable** if there exists an object $X^*$ (its dual) and morphisms:
- Unit: $I \to X \otimes X^*$,
- Counit: $X^* \otimes X \to I$,
satisfying the zigzag identities.

---

### Fully dualizable object  
In a symmetric monoidal (∞,n)-category, an object is **fully dualizable** if it has duals at all levels up to n-morphisms. This concept is central to the cobordism hypothesis.

---

### Serre duality  
In algebraic geometry, **Serre duality** is a duality between sheaf cohomology groups of a smooth projective variety $X$, given by:
$$
H^i(X, \mathcal{F}) \cong H^{n-i}(X, \omega_X \otimes \mathcal{F}^\vee)^*.
$$

---

### Verdier duality  
**Verdier duality** is a generalization of Poincaré duality in sheaf theory, providing a duality between derived categories of sheaves on locally compact spaces.

---

### Grothendieck duality  
**Grothendieck duality** is a powerful framework extending Serre and Verdier duality to non-smooth and relative settings, especially in derived algebraic geometry.

---

## ✅ MONADS & ALGEBRAS

### Monad in a bicategory  
A **monad in a bicategory** $\mathcal{B}$ consists of:
- An object $A$,
- A 1-cell $T : A \to A$,
- 2-cells $\mu : T T \Rightarrow T$, $\eta : \text{id}_A \Rightarrow T$,
satisfying associativity and unit laws.

---

### Comonad  
A **comonad** is the dual of a monad: it consists of a 1-cell $C : A \to A$ with comultiplication and counit 2-cells satisfying coassociativity and counitality.

---

### Eilenberg–Moore object  
The **Eilenberg–Moore object** of a monad $T$ in a bicategory is the universal object representing algebras over $T$, analogous to the category of algebras over a monad.

---

### Kleisli object  
The **Kleisli object** of a monad $T$ is the universal object representing free algebras over $T$, analogous to the Kleisli category.

---

### Distributive law  
A **distributive law** between two monads $S$ and $T$ is a natural transformation $ST \Rightarrow TS$ satisfying coherence conditions that allow the composite $TS$ to become a monad.

---

### Algebras for a monad  
Given a monad $T$ on a category $\mathcal{C}$, an **algebra for $T$** (or **T-algebra**) is an object $A \in \mathcal{C}$ together with a morphism $a : TA \to A$ satisfying associativity and unit axioms.

---

### Coalgebras  
Coalgebras are the dual notion of algebras: they consist of an object $C$ with a coaction $C \to TC$, satisfying coassociativity and counitality.

---

### Monadic functor  
A **monadic functor** is a functor $U : \mathcal{D} \to \mathcal{C}$ that is equivalent to the forgetful functor from the category of algebras over a monad.

---

### Barr–Beck theorem  
The **Barr–Beck theorem** gives necessary and sufficient conditions for a functor $U : \mathcal{D} \to \mathcal{C}$ to be monadic, i.e., to exhibit $\mathcal{D}$ as the category of algebras over a monad on $\mathcal{C}$.

---

### Lax algebra  
A **lax algebra** over a monad $T$ in a bicategory is a generalization of an algebra where the action is only lax compatible with the monad structure.

---

### Pseudo-monad  
A **pseudo-monad** is a monad-like structure in a bicategory where the monad axioms hold only up to coherent invertible 2-cells.

---

### Pseudo-algebra  
A **pseudo-algebra** over a pseudo-monad is a structure where the algebra axioms hold up to invertible 2-cells.

---
Absolutely! Let's continue with the **mathematically precise definitions** for the remaining categories:

---

## ✅ OPERADS & ALGEBRAIC STRUCTURES

### Operad  
An **operad** $\mathcal{O}$ is a collection of sets (or objects in a symmetric monoidal category) $\mathcal{O}(n)$, indexed by natural numbers $n \geq 0$, equipped with:
- A right action of the symmetric group $S_n$ on each $\mathcal{O}(n)$,
- Composition maps $\circ_i : \mathcal{O}(k) \times \mathcal{O}(m) \to \mathcal{O}(k + m - 1)$,
satisfying associativity, equivariance, and unit axioms.

Operads encode algebraic structures with operations of multiple inputs.

---

### Multicategory  
A **multicategory** generalizes a category by allowing morphisms to have multiple inputs: a morphism $f : (X_1,\dots,X_n) \to Y$. Composition is defined by plugging outputs into inputs.

Operads are special cases of multicategories with only one object.

---

### PROP  
A **PROP** (Product and Permutation category) is a symmetric monoidal category whose objects are the natural numbers, and where the tensor product is given by addition. PROPs encode algebraic structures with both operations and co-operations.

---

### Lawvere theory  
(Already defined under Classical Category Theory.)

---

### Topological operad  
A **topological operad** is an operad internal to the category of topological spaces, where all composition maps and symmetric actions are continuous.

---

### Symmetric operad  
A **symmetric operad** is an operad equipped with a compatible action of the symmetric groups on its components.

---

### Cyclic operad  
A **cyclic operad** is an operad equipped with an additional cyclic symmetry on its operations, allowing the output to be rotated to any input.

---

### Modular operad  
A **modular operad** extends the notion of operad to allow compositions along graphs (not just trees), modeling operations with genus and allowing self-gluing.

---

### Algebra over an operad  
Given an operad $\mathcal{O}$ in a symmetric monoidal category $\mathcal{C}$, an **algebra over $\mathcal{O}$** is an object $A \in \mathcal{C}$ together with a morphism of operads $\mathcal{O} \to \mathrm{End}(A)$, where $\mathrm{End}(A)(n) = \mathcal{C}(A^{\otimes n}, A)$.

---

### Coalgebra over an operad  
Dually, a **coalgebra over an operad** is an object $C$ together with a morphism of operads $\mathcal{O} \to \mathrm{CoEnd}(C)$, where $\mathrm{CoEnd}(C)(n) = \mathcal{C}(C, C^{\otimes n})$.

---

### ∞-operad  
An **∞-operad** is a higher categorical analog of an operad, typically modeled as a fibration over the category of finite pointed sets satisfying certain Segal conditions. It encodes homotopy-coherent algebraic structures.

---

### Dendroidal set  
A **dendroidal set** is a presheaf on the category $\Omega$ of rooted trees. It generalizes simplicial sets to model ∞-operads.

---

### Colored operad  
A **colored operad** (also called a **multicategory**) allows multiple "colors" or types of inputs and outputs. Each operation has a list of input colors and a single output color.

---

### Properad  
A **properad** generalizes operads by allowing operations with multiple inputs and multiple outputs, composed via directed graphs (not just trees). They model bialgebra-like structures.

---

### ∞-properad  
An **∞-properad** is a properad in the context of higher category theory, often defined as a dendroidal space or a Segal properad satisfying appropriate fibrancy conditions.

---

## ✅ TOPOLOGY & HOMOTOPY THEORY

### Classifying space  
The **classifying space** $BG$ of a topological group $G$ is a space such that its fundamental group is $G$ and all higher homotopy groups vanish. It classifies principal $G$-bundles.

More generally, the classifying space of a small category $\mathcal{C}$ is the geometric realization of its nerve.

---

### Delooping  
To **deloop** a group $G$ means to construct a space $BG$ such that $\Omega BG \simeq G$. In higher category theory, delooping a monoid or groupoid yields a one-object category or ∞-groupoid.

---

### Loop space  
The **loop space** $\Omega X$ of a pointed space $X$ is the space of based loops in $X$, i.e., continuous maps $S^1 \to X$ sending the basepoint to the basepoint of $X$.

In higher category theory, it corresponds to the automorphism space of the basepoint in the ∞-groupoid of $X$.

---

### Loop space object  
In an (∞,1)-category with a terminal object, the **loop space object** $\Omega X$ of a pointed object $X$ is the pullback of the diagram $* \to X \leftarrow *$.

---

### Mapping space  
The **mapping space** $\mathrm{Map}(X,Y)$ between two objects in an (∞,1)-category is the ∞-groupoid of morphisms from $X$ to $Y$, capturing all higher homotopies between them.

---

### Fundamental ∞-groupoid  
The **fundamental ∞-groupoid** $\Pi_\infty(X)$ of a topological space $X$ is the ∞-groupoid whose $k$-morphisms are homotopy classes of $k$-dimensional paths in $X$.

It represents the homotopy type of $X$.

---

### Homotopy fiber  
The **homotopy fiber** of a map $f : X \to Y$ at a point $y \in Y$ is the space of pairs $(x, p)$ where $x \in X$ and $p$ is a path from $f(x)$ to $y$.

In higher category theory, it is the pullback of the diagram $* \xrightarrow{y} Y \xleftarrow{f} X$.

---

### Homotopy n-type  
A **homotopy n-type** is a space whose homotopy groups vanish above degree $n$. The category of homotopy n-types is equivalent to the category of n-groupoids.

---

### Homotopy quotient  
The **homotopy quotient** $X//G$ of a $G$-space $X$ is the Borel construction $EG \times_G X$, which resolves the naive quotient $X/G$ by replacing it with a space that accounts for the homotopy orbits.

---

### Stabilization  
The **stabilization** of an ∞-category $\mathcal{C}$ with finite limits is the ∞-category $\mathrm{Sp}(\mathcal{C})$ of spectrum objects in $\mathcal{C}$, representing stable phenomena like loop spaces iterated infinitely.

---

### Suspension  
The **suspension** $\Sigma X$ of a pointed space $X$ is the quotient space $X \times [0,1] / (X \times \{0\} \cup \{*\} \times [0,1] \cup X \times \{1\})$.

In higher category theory, it is the left adjoint to the loop space functor.

---

## ✅ DIMENSIONAL ENHANCEMENTS

### 2-category  
A **2-category** is a category enriched over the monoidal category $\mathbf{Cat}$ of small categories. It consists of:
- Objects,
- 1-morphisms between objects (forming categories),
- 2-morphisms between 1-morphisms (natural transformations),
with strict composition in both dimensions.

Examples include $\mathbf{Cat}$, the 2-category of small categories, functors, and natural transformations.

---

### 3-category  
A **3-category** is a category enriched over the monoidal category of 2-categories. It has:
- Objects,
- 1-morphisms,
- 2-morphisms,
- 3-morphisms (modifications),
with strict compositions across all levels.

This can be extended to higher $n$-categories recursively.

---

### n-fold category  
An **n-fold category** (also called an **n-tuple category**) is a category internal to $(n-1)$-fold categories. It generalizes double and triple categories, with $n$ independent directions of morphisms.

It can be visualized as an $n$-dimensional grid of morphisms.

---

### Iterated span category  
An **iterated span category** is built by iteratively taking spans: a span from $X$ to $Y$ is a diagram $X \leftarrow S \to Y$. The **category of spans** becomes a 2-category when equipped with maps between spans, and this can be iterated to form an (∞,n)-category.

---

### Gray-category  
A **Gray-category** is a semi-strict 3-category where the interchange law for horizontal composition of 2-cells holds only up to coherent isomorphism. It provides a manageable model for weak 3-categories.

---

### Trimble n-category  
A **Trimble n-category** is a definition of weak n-category using operadic techniques and topological enrichment. It starts from topological spaces and iteratively defines higher categorical structures via coherences encoded in operads.

---

### Tamsamani n-category  
A **Tamsamani n-category** is defined inductively using simplicial objects in the category of Tamsamani $(n-1)$-categories. It satisfies Segal-type conditions that ensure coherence.

---

### Street nerve  
The **nerve of a strict ω-category** (Street nerve) is a simplicial set encoding its structure. It generalizes the nerve of a category and plays a role in defining complicial sets.

---

### Θ-space  
A **Θ-space** is a presheaf on Joyal’s category $\Theta_n$, used to model (∞,n)-categories. It combines simplicial and globular ideas and satisfies Segal and completeness conditions.

---

### Rezk completion  
The **Rezk completion** (or **fibrant replacement**) of a Segal space $X$ is a complete Segal space $RX$ obtained by formally inverting equivalences in $X_0$, making equivalent objects equal.

It ensures that the space of objects reflects the actual ∞-groupoid of objects.

---

### Homotopy coherent nerve  
The **homotopy coherent nerve** $\mathrm{N}(\mathcal{C})$ of a simplicial category $\mathcal{C}$ is a simplicial set whose $n$-simplices are homotopy coherent diagrams of shape $[n]$. It models the ∞-category associated to $\mathcal{C}$.

---

### ω-category  
(Already defined under Types of Higher Categories.)

---

## ✅ ALGEBRAIC GEOMETRY & PHYSICS

### Derived stack  
A **derived stack** is a stack in derived algebraic geometry, typically defined as a sheaf of ∞-groupoids on a site of derived affine schemes. It allows one to encode not just geometric data but also derived information like deformation theory.

---

### Higher stack  
A **higher stack** is a generalization of a stack taking values in ∞-groupoids rather than sets or groupoids. It captures higher descent data and is central in derived and nonabelian geometry.

---

### Perfect stack  
A **perfect stack** is a derived stack where the category of quasi-coherent sheaves is generated by perfect complexes. These are important in geometric representation theory and topological field theory.

---

### Geometric Langlands program  
The **geometric Langlands program** is a geometric analog of the classical Langlands program. It relates categories of D-modules on moduli stacks of bundles on a curve to categories of coherent sheaves on the stack of local systems.

---

### Topological field theory  
A **topological field theory (TFT)** is a symmetric monoidal functor from a bordism category of manifolds to a symmetric monoidal ∞-category (often of vector spaces or spectra). It assigns invariants to manifolds independent of smooth structure.

---

### Extended TQFT  
An **extended topological quantum field theory (TQFT)** is a symmetric monoidal (∞,n)-functor from the (∞,n)-category of cobordisms to a target symmetric monoidal (∞,n)-category (e.g., of n-vector spaces).

It assigns data not just to n-manifolds and (n−1)-manifolds, but to all lower-dimensional strata.

---

### Conformal field theory  
A **conformal field theory (CFT)** is a quantum field theory invariant under conformal transformations. In mathematical physics, it is often modeled using vertex algebras or modular tensor categories.

---

### Factorization algebra  
A **factorization algebra** is a cosheaf-like structure on a manifold assigning algebras to open subsets, with multiplication maps indexed by disjoint inclusions. It encodes the observables of a quantum field theory.

---

### Chiral algebra  
A **chiral algebra** on a complex curve is a Lie algebra object in the category of D-modules with a certain chiral bracket. It arises naturally in 2D conformal field theory and the geometric Langlands program.

---

### Vertex operator algebra  
A **vertex operator algebra (VOA)** is an algebraic structure encoding the symmetries of a 2D conformal field theory. It includes a state-field correspondence and a notion of operator product expansion.

---

### Deformation quantization  
**Deformation quantization** is a formal procedure that associates a noncommutative algebra (or sheaf of algebras) to a Poisson manifold, deforming the commutative algebra of functions into a star-product.

---

### Drinfeld center  
The **Drinfeld center** $\mathcal{Z}(\mathcal{C})$ of a monoidal category $\mathcal{C}$ is the braided monoidal category whose objects are pairs $(X, \sigma_{-,X})$, where $\sigma$ is a half-braiding satisfying naturality and hexagon axioms.

In higher categories, it generalizes to the center of a monoidal ∞-category.

---

### Hochschild cohomology  
The **Hochschild cohomology** $HH^*(A,A)$ of an algebra $A$ classifies deformations of $A$. For a dg-category or stable ∞-category, it generalizes to a spectrum or graded ring controlling autoequivalences and deformations.

---

### Cyclic homology  
**Cyclic homology** is a variant of Hochschild homology that incorporates a circle action. It appears naturally in noncommutative geometry and string topology.

---

### A∞-algebra  
An **A∞-algebra** is a graded vector space $A$ equipped with a sequence of multilinear operations $m_n : A^{\otimes n} \to A$ of degree $2 - n$, satisfying generalized associativity constraints encoded by the Stasheff polytopes.

It is the homotopy-coherent version of an associative algebra.

---

### A∞-category  
An **A∞-category** is a many-object version of an A∞-algebra: it has objects, morphism spaces, and higher composition maps satisfying analogous coherence conditions.

It is widely used in symplectic geometry and mirror symmetry.

---

### L∞-algebra  
An **L∞-algebra** is a graded vector space with a sequence of skew-symmetric brackets of varying arity, satisfying generalized Jacobi identities up to coherent homotopy.

It is the homotopy-coherent version of a Lie algebra.

---

### dg-category  
A **differential graded (dg) category** is a category enriched over chain complexes of abelian groups. Composition is bilinear and respects the differential.

These are foundational in noncommutative geometry and derived algebraic geometry.

---

### Spectral category  
A **spectral category** is a category enriched over spectra. It generalizes dg-categories to the world of stable homotopy theory and is used in derived algebraic geometry and noncommutative motives.

---

### Shifted symplectic structure  
A **k-shifted symplectic structure** on a derived Artin stack $X$ is a closed 2-form of degree $k$ that is non-degenerate in a derived sense. These generalize classical symplectic structures and appear in derived algebraic geometry and shifted Poisson geometry.

---

### Factorization homology  
**Factorization homology** is a topological invariant of manifolds valued in a symmetric monoidal ∞-category, constructed by integrating an E_n-algebra over a framed n-manifold.


