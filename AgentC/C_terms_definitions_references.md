I'll append scholarly references to each definition. This will be quite extensive, but I'll provide legitimate mathematical sources for each term.

## Classical Category Theory

### Abelian category
An abelian category is a pre-abelian category $\mathcal{A}$ satisfying:
- Every monomorphism is a kernel of some morphism
- Every epimorphism is a cokernel of some morphism
- Every morphism can be factored as an epimorphism followed by a monomorphism

**Reference**: Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Graduate Texts in Mathematics, vol. 5. Springer-Verlag. Chapter VIII.

### Additive category
An additive category is a category $\mathcal{C}$ enriched over abelian groups such that:
- $\mathcal{C}$ has a zero object $0$
- $\mathcal{C}$ has all finite biproducts (equivalently, all finite products and coproducts that coincide)

**Reference**: Borceux, F. (1994). *Handbook of Categorical Algebra 2: Categories and Structures*. Encyclopedia of Mathematics and its Applications, vol. 51. Cambridge University Press. Section 1.2.

### Adjoint functor theorem
**Freyd's General Adjoint Functor Theorem**: A functor $G: \mathcal{D} \to \mathcal{C}$ has a left adjoint if and only if:
1. $G$ preserves all limits that exist in $\mathcal{D}$
2. For each $c \in \mathcal{C}$, the comma category $(c \downarrow G)$ satisfies the solution set condition

**Reference**: Freyd, P. (1964). *Abelian Categories*. Harper & Row. Reprinted in: Reprints in Theory and Applications of Categories, No. 3 (2003) pp. 1-190.

### Adjunction
An adjunction consists of functors $L: \mathcal{C} \rightleftarrows \mathcal{D} : R$ with natural isomorphism:
$$\text{Hom}_{\mathcal{D}}(L(c), d) \cong \text{Hom}_{\mathcal{C}}(c, R(d))$$
The unit $\eta: \text{id}_\mathcal{C} \Rightarrow R \circ L$ and counit $\epsilon: L \circ R \Rightarrow \text{id}_\mathcal{D}$ satisfy the triangle identities.

**Reference**: Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Graduate Texts in Mathematics, vol. 5. Springer-Verlag. Chapter IV.

### Automorphism
An automorphism of an object $X$ in a category $\mathcal{C}$ is an isomorphism $f: X \to X$.

**Reference**: Awodey, S. (2010). *Category Theory* (2nd ed.). Oxford Logic Guides, vol. 52. Oxford University Press. Section 2.1.

### Balanced category
A category $\mathcal{C}$ is balanced if every morphism that is both monic and epic is an isomorphism.

**Reference**: Borceux, F. (1994). *Handbook of Categorical Algebra 1: Basic Category Theory*. Encyclopedia of Mathematics and its Applications, vol. 50. Cambridge University Press. Definition 1.7.7.

### Category
A category $\mathcal{C}$ consists of:
- A collection $\text{Ob}(\mathcal{C})$ of objects
- For each pair $(A,B)$ of objects, a collection $\text{Hom}_\mathcal{C}(A,B)$ of morphisms
- Composition $\circ: \text{Hom}(B,C) \times \text{Hom}(A,B) \to \text{Hom}(A,C)$
- Identity morphisms $\text{id}_A: A \to A$

satisfying associativity and unit laws. Small if $\text{Ob}(\mathcal{C})$ is a set; locally small if each $\text{Hom}(A,B)$ is a set.

**Reference**: Eilenberg, S. & Mac Lane, S. (1945). "General theory of natural equivalences". *Transactions of the American Mathematical Society*, 58(2), 231-294.

### Category of elements
For a functor $F: \mathcal{C} \to \mathbf{Set}$, the category of elements $\int F$ has:
- Objects: pairs $(c, x)$ where $c \in \mathcal{C}$ and $x \in F(c)$
- Morphisms $(c, x) \to (d, y)$: morphisms $f: c \to d$ such that $F(f)(x) = y$

**Reference**: Mac Lane, S. & Moerdijk, I. (1994). *Sheaves in Geometry and Logic*. Universitext. Springer-Verlag. Section III.5.

### Cauchy (Karoubi) completion
The Cauchy completion $\overline{\mathcal{C}}$ of a category $\mathcal{C}$ has:
- Objects: idempotents $(e: A \to A)$ in $\mathcal{C}$
- Morphisms $(e: A \to A) \to (e': B \to B)$: morphisms $f: A \to B$ such that $f = e' \circ f \circ e$

**Reference**: Karoubi, M. (1978). *K-Theory: An Introduction*. Grundlehren der mathematischen Wissenschaften, vol. 226. Springer-Verlag. Chapter 1.

### Comma category
For functors $F: \mathcal{A} \to \mathcal{C}$ and $G: \mathcal{B} \to \mathcal{C}$, the comma category $(F \downarrow G)$ has:
- Objects: triples $(a, f, b)$ where $a \in \mathcal{A}$, $b \in \mathcal{B}$, and $f: F(a) \to G(b)$
- Morphisms $(a, f, b) \to (a', f', b')$: pairs $(h: a \to a', k: b \to b')$ making the obvious square commute

**Reference**: Lawvere, F.W. (1963). "Functorial semantics of algebraic theories". *Proceedings of the National Academy of Sciences*, 50(5), 869-872.

### Composition
Composition in a category is the operation $\circ: \text{Hom}(B,C) \times \text{Hom}(A,B) \to \text{Hom}(A,C)$ satisfying:
- Associativity: $(h \circ g) \circ f = h \circ (g \circ f)$
- Identity laws: $f \circ \text{id}_A = f = \text{id}_B \circ f$ for $f: A \to B$

**Reference**: Leinster, T. (2014). *Basic Category Theory*. Cambridge Studies in Advanced Mathematics, vol. 143. Cambridge University Press. Section 1.1.

### Contravariant functor
A contravariant functor $F: \mathcal{C} \to \mathcal{D}$ is a functor $F: \mathcal{C}^{op} \to \mathcal{D}$, reversing the direction of morphisms.

**Reference**: Riehl, E. (2016). *Category Theory in Context*. Dover Publications. Section 1.3.

### Copower
The copower of an object $A$ by a set $S$, denoted $S \cdot A$, is the coproduct $\coprod_{s \in S} A$.

**Reference**: Kelly, G.M. (1982). *Basic Concepts of Enriched Category Theory*. London Mathematical Society Lecture Note Series, vol. 64. Cambridge University Press. Section 1.4.

### Copresheaf
A copresheaf on $\mathcal{C}$ is a functor $F: \mathcal{C} \to \mathbf{Set}$.

**Reference**: Kashiwara, M. & Schapira, P. (2006). *Categories and Sheaves*. Grundlehren der mathematischen Wissenschaften, vol. 332. Springer-Verlag. Section 1.4.

### Coproduct
The coproduct $\coprod_{i \in I} A_i$ is the colimit of the discrete diagram $\{A_i\}_{i \in I}$, with injections $\iota_j: A_j \to \coprod_{i \in I} A_i$.

**Reference**: Adámek, J., Herrlich, H., & Strecker, G.E. (1990). *Abstract and Concrete Categories*. John Wiley & Sons. Section 11.

### Cosegment
A cosegment object is an object $X$ with two morphisms $s, t: \ast \to X$ from the terminal object.

**Reference**: Lawvere, F.W. & Schanuel, S.H. (2009). *Conceptual Mathematics: A First Introduction to Categories* (2nd ed.). Cambridge University Press. Chapter 13.

### Coslice category
The coslice category $c/\mathcal{C}$ for $c \in \mathcal{C}$ has:
- Objects: morphisms $f: c \to d$ in $\mathcal{C}$
- Morphisms: commutative triangles

**Reference**: Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Graduate Texts in Mathematics, vol. 5. Springer-Verlag. Section II.6.

### Coequalizer
The coequalizer of $f, g: A \rightrightarrows B$ is the colimit of this diagram, giving $q: B \to C$ with $q \circ f = q \circ g$ universal.

**Reference**: Barr, M. & Wells, C. (1995). *Category Theory for Computing Science* (2nd ed.). Prentice Hall. Chapter 8.

### Coefficient
In enriched category theory, coefficients refer to the enriching category $\mathcal{V}$.

**Reference**: Kelly, G.M. (1982). *Basic Concepts of Enriched Category Theory*. London Mathematical Society Lecture Note Series, vol. 64. Cambridge University Press. Section 1.1.

### Coend
For a functor $F: \mathcal{C}^{op} \times \mathcal{C} \to \mathcal{D}$, the coend is:
$$\int^{c \in \mathcal{C}} F(c,c) = \text{coeq}\left(\coprod_{f: c \to c'} F(c',c) \rightrightarrows \coprod_{c} F(c,c)\right)$$

**Reference**: Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Graduate Texts in Mathematics, vol. 5. Springer-Verlag. Section IX.6.

### Coreflective subcategory
A full subcategory $\mathcal{D} \hookrightarrow \mathcal{C}$ is coreflective if the inclusion has a right adjoint.

**Reference**: Adámek, J. & Rosický, J. (1994). *Locally Presentable and Accessible Categories*. London Mathematical Society Lecture Note Series, vol. 189. Cambridge University Press. Section 1.36.

### Covariant functor
A covariant functor $F: \mathcal{C} \to \mathcal{D}$ preserves the direction of morphisms: $F(f: A \to B) = F(f): F(A) \to F(B)$.

**Reference**: Awodey, S. (2010). *Category Theory* (2nd ed.). Oxford Logic Guides, vol. 52. Oxford University Press. Section 7.1.

### Dinatural transformation
A dinatural transformation $\alpha: F \Rightarrow G$ between functors $F, G: \mathcal{C}^{op} \times \mathcal{C} \to \mathcal{D}$ consists of components $\alpha_c: F(c,c) \to G(c,c)$ satisfying the hexagon identity.

**Reference**: Dubuc, E.J. & Street, R. (1970). "Dinatural transformations". In: *Reports of the Midwest Category Seminar IV*, Lecture Notes in Mathematics, vol. 137, pp. 126-137. Springer-Verlag.

### Dual category
The dual (opposite) category $\mathcal{C}^{op}$ has the same objects as $\mathcal{C}$ with $\text{Hom}_{\mathcal{C}^{op}}(A,B) = \text{Hom}_\mathcal{C}(B,A)$.

**Reference**: Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Graduate Texts in Mathematics, vol. 5. Springer-Verlag. Section II.2.

### End
For a functor $F: \mathcal{C}^{op} \times \mathcal{C} \to \mathcal{D}$, the end is:
$$\int_{c \in \mathcal{C}} F(c,c) = \text{eq}\left(\prod_{c} F(c,c) \rightrightarrows \prod_{f: c \to c'} F(c',c)\right)$$

**Reference**: Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Graduate Texts in Mathematics, vol. 5. Springer-Verlag. Section IX.5.

### Equalizer
The equalizer of $f, g: A \rightrightarrows B$ is the limit of this diagram, giving $e: E \to A$ with $f \circ e = g \circ e$ universal.

**Reference**: Borceux, F. (1994). *Handbook of Categorical Algebra 1: Basic Category Theory*. Encyclopedia of Mathematics and its Applications, vol. 50. Cambridge University Press. Section 2.5.

### Essentially surjective functor
A functor $F: \mathcal{C} \to \mathcal{D}$ is essentially surjective if for every $d \in \mathcal{D}$, there exists $c \in \mathcal{C}$ with $F(c) \cong d$.

**Reference**: Johnstone, P.T. (2002). *Sketches of an Elephant: A Topos Theory Compendium*. Oxford Logic Guides, vols. 43-44. Oxford University Press. Section A1.1.

### Exact category
An exact category is an additive category with a class of short exact sequences satisfying the axioms of Quillen.

**Reference**: Quillen, D. (1973). "Higher algebraic K-theory: I". In: *Algebraic K-Theory I*, Lecture Notes in Mathematics, vol. 341, pp. 85-147. Springer-Verlag.

### Factorization system
A factorization system $(\mathcal{E}, \mathcal{M})$ on $\mathcal{C}$ consists of classes of morphisms such that:
- Every morphism factors as $f = m \circ e$ with $e \in \mathcal{E}$, $m \in \mathcal{M}$
- $\mathcal{E}$ and $\mathcal{M}$ satisfy the unique diagonal fill-in property

**Reference**: Freyd, P.J. & Kelly, G.M. (1972). "Categories of continuous functors, I". *Journal of Pure and Applied Algebra*, 2(3), 169-191.

### Fully faithful functor
A functor $F: \mathcal{C} \to \mathcal{D}$ is fully faithful if each function $F_{A,B}: \text{Hom}_\mathcal{C}(A,B) \to \text{Hom}_\mathcal{D}(F(A),F(B))$ is bijective.

**Reference**: Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Graduate Texts in Mathematics, vol. 5. Springer-Verlag. Section I.3.

### Functor
A functor $F: \mathcal{C} \to \mathcal{D}$ consists of:
- Object function $F: \text{Ob}(\mathcal{C}) \to \text{Ob}(\mathcal{D})$
- Morphism functions $F_{A,B}: \text{Hom}_\mathcal{C}(A,B) \to \text{Hom}_\mathcal{D}(F(A),F(B))$
preserving composition and identities.

**Reference**: Eilenberg, S. & Mac Lane, S. (1945). "General theory of natural equivalences". *Transactions of the American Mathematical Society*, 58(2), 231-294.

### Functor category
The functor category $[\mathcal{C}, \mathcal{D}]$ has functors $F: \mathcal{C} \to \mathcal{D}$ as objects and natural transformations as morphisms.

**Reference**: Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Graduate Texts in Mathematics, vol. 5. Springer-Verlag. Section II.4.

### Full functor
A functor $F: \mathcal{C} \to \mathcal{D}$ is full if each function $F_{A,B}: \text{Hom}_\mathcal{C}(A,B) \to \text{Hom}_\mathcal{D}(F(A),F(B))$ is surjective.

**Reference**: Awodey, S. (2010). *Category Theory* (2nd ed.). Oxford Logic Guides, vol. 52. Oxford University Press. Section 7.4.

### Grothendieck fibration
A functor $p: \mathcal{E} \to \mathcal{B}$ is a Grothendieck fibration if for every $e \in \mathcal{E}$ and morphism $f: b \to p(e)$ in $\mathcal{B}$, there exists a cartesian lifting of $f$ at $e$.

**Reference**: Grothendieck, A. (1971). *Revêtements étales et groupe fondamental (SGA 1)*. Lecture Notes in Mathematics, vol. 224. Springer-Verlag. Exposé VI.

### Grothendieck topology
A Grothendieck topology on $\mathcal{C}$ assigns to each object $c$ a collection $J(c)$ of sieves (covering families) satisfying stability, transitivity, and identity axioms.

**Reference**: Artin, M., Grothendieck, A., & Verdier, J.L. (1972). *Théorie des topos et cohomologie étale des schémas (SGA 4)*. Lecture Notes in Mathematics, vols. 269-270-305. Springer-Verlag.

### Image
The image of $f: A \to B$ is the smallest subobject of $B$ through which $f$ factors.

**Reference**: Mitchell, B. (1965). *Theory of Categories*. Pure and Applied Mathematics, vol. 17. Academic Press. Chapter III.

### Initial object
An object $0 \in \mathcal{C}$ is initial if for every object $A$, there exists a unique morphism $0 \to A$.

**Reference**: Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Graduate Texts in Mathematics, vol. 5. Springer-Verlag. Section III.2.

### Isomorphism
A morphism $f: A \to B$ is an isomorphism if there exists $g: B \to A$ with $g \circ f = \text{id}_A$ and $f \circ g = \text{id}_B$.

**Reference**: Leinster, T. (2014). *Basic Category Theory*. Cambridge Studies in Advanced Mathematics, vol. 143. Cambridge University Press. Section 1.1.

### Kan extension
The left Kan extension of $F: \mathcal{C} \to \mathcal{E}$ along $K: \mathcal{C} \to \mathcal{D}$ is the left adjoint to the restriction functor $[\mathcal{D}, \mathcal{E}] \to [\mathcal{C}, \mathcal{E}]$ given by precomposition with $K$.

**Reference**: Kan, D.M. (1958). "Adjoint functors". *Transactions of the American Mathematical Society*, 87(2), 294-329.

### Kernel
The kernel of $f: A \to B$ in an abelian category is the equalizer of $f$ and the zero morphism $0: A \to B$.

**Reference**: Freyd, P. (1964). *Abelian Categories*. Harper & Row. Reprinted in: Reprints in Theory and Applications of Categories, No. 3 (2003) pp. 1-190.

### Lawvere theory
A Lawvere theory is a small category $\mathcal{T}$ with finite products and a strict finite-product-preserving functor $\mathcal{F}^{op} \to \mathcal{T}$ from the opposite of the category of finite sets.

**Reference**: Lawvere, F.W. (1963). "Functorial semantics of algebraic theories". *Proceedings of the National Academy of Sciences*, 50(5), 869-872.

### Limit
The limit of a functor $F: \mathcal{J} \to \mathcal{C}$ is an object $\lim F$ with a cone $\pi_j: \lim F \to F(j)$ universal among all cones over $F$.

**Reference**: Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Graduate Texts in Mathematics, vol. 5. Springer-Verlag. Chapter III.

### Locally presentable category
A category $\mathcal{C}$ is locally presentable if it is cocomplete and has a set of $\kappa$-compact objects generating $\mathcal{C}$ under $\kappa$-filtered colimits for some regular cardinal $\kappa$.

**Reference**: Gabriel, P. & Ulmer, F. (1971). *Lokal präsentierbare Kategorien*. Lecture Notes in Mathematics, vol. 221. Springer-Verlag.

### Monomorphism
A morphism $f: A \to B$ is a monomorphism if $f \circ g = f \circ h$ implies $g = h$ for all $g, h: C \to A$.

**Reference**: Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Graduate Texts in Mathematics, vol. 5. Springer-Verlag. Section I.5.

### Multicategory
A multicategory has objects and multimorphisms $(A_1, \ldots, A_n) \to B$ with composition and identities satisfying appropriate axioms.

**Reference**: Leinster, T. (2004). *Higher Operads, Higher Categories*. London Mathematical Society Lecture Note Series, vol. 298. Cambridge University Press. Chapter 2.

### Natural transformation
A natural transformation $\alpha: F \Rightarrow G$ between functors $F, G: \mathcal{C} \to \mathcal{D}$ consists of components $\alpha_c: F(c) \to G(c)$ such that for all $f: c \to c'$, we have $G(f) \circ \alpha_c = \alpha_{c'} \circ F(f)$.

**Reference**: Eilenberg, S. & Mac Lane, S. (1945). "General theory of natural equivalences". *Transactions of the American Mathematical Society*, 58(2), 231-294.

### Natural isomorphism
A natural transformation $\alpha: F \Rightarrow G$ is a natural isomorphism if each component $\alpha_c$ is an isomorphism.

**Reference**: Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Graduate Texts in Mathematics, vol. 5. Springer-Verlag. Section II.4.

### Nerve of a category
The nerve $N(\mathcal{C})$ of a category $\mathcal{C}$ is the simplicial set with $N(\mathcal{C})_n$ = composable sequences of $n$ morphisms in $\mathcal{C}$.

**Reference**: Segal, G. (1974). "Categories and cohomology theories". *Topology*, 13(3), 293-312.

### Opposite category
Same as dual category: $\mathcal{C}^{op}$ with reversed morphisms.

**Reference**: Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Graduate Texts in Mathematics, vol. 5. Springer-Verlag. Section II.2.

### Power
The power $A^S$ is the product $\prod_{s \in S} A$, representing the internal hom $[S, A]$ when it exists.

**Reference**: Kelly, G.M. (1982). *Basic Concepts of Enriched Category Theory*. London Mathematical Society Lecture Note Series, vol. 64. Cambridge University Press. Section 1.4.

### Preadditive category
A category enriched over abelian groups, i.e., each hom-set has an abelian group structure compatible with composition.

**Reference**: Mitchell, B. (1965). *Theory of Categories*. Pure and Applied Mathematics, vol. 17. Academic Press. Chapter II.

### Product
The product $\prod_{i \in I} A_i$ is the limit of the discrete diagram $\{A_i\}_{i \in I}$, with projections $\pi_j: \prod_{i \in I} A_i \to A_j$.

**Reference**: Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Graduate Texts in Mathematics, vol. 5. Springer-Verlag. Section III.3.

### Pullback
The pullback of $f: A \to C$ and $g: B \to C$ is the limit of the cospan diagram, yielding $P$ with morphisms to $A$ and $B$ making the square commute.

**Reference**: Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Graduate Texts in Mathematics, vol. 5. Springer-Verlag. Section III.4.

### Pushout
The pushout of $f: C \to A$ and $g: C \to B$ is the colimit of the span diagram.

**Reference**: Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Graduate Texts in Mathematics, vol. 5. Springer-Verlag. Section III.4.

### Reflective subcategory
A full subcategory $\mathcal{D} \hookrightarrow \mathcal{C}$ is reflective if the inclusion has a left adjoint.

**Reference**: Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Graduate Texts in Mathematics, vol. 5. Springer-Verlag. Section IV.3.

### Representable functor
A functor $F: \mathcal{C}^{op} \to \mathbf{Set}$ is representable if $F \cong \text{Hom}_\mathcal{C}(-, c)$ for some $c \in \mathcal{C}$.

**Reference**: Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Graduate Texts in Mathematics, vol. 5. Springer-Verlag. Section III.2.

### Retract
An object $A$ is a retract of $B$ if there exist $i: A \to B$ and $r: B \to A$ with $r \circ i = \text{id}_A$.

**Reference**: May, J.P. (1999). *A Concise Course in Algebraic Topology*. Chicago Lectures in Mathematics. University of Chicago Press. Chapter 1.

### Slice category
The slice category $\mathcal{C}/c$ for $c \in \mathcal{C}$ has:
- Objects: morphisms $f: d \to c$ in $\mathcal{C}$
- Morphisms: commutative triangles

**Reference**: Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Graduate Texts in Mathematics, vol. 5. Springer-Verlag. Section II.6.

### Split exact sequence
An exact sequence $0 \to A \xrightarrow{i} B \xrightarrow{p} C \to 0$ splits if there exist $r: B \to A$ and $s: C \to B$ with $r \circ i = \text{id}_A$ and $p \circ s = \text{id}_C$.

**Reference**: Weibel, C.A. (1994). *An Introduction to Homological Algebra*. Cambridge Studies in Advanced Mathematics, vol. 38. Cambridge University Press. Section 1.4.

### Split monomorphism / split epimorphism
A monomorphism $f: A \to B$ splits if there exists $g: B \to A$ with $g \circ f = \text{id}_A$. Dually for split epimorphisms.

**Reference**: Borceux, F. (1994). *Handbook of Categorical Algebra 1: Basic Category Theory*. Encyclopedia of Mathematics and its Applications, vol. 50. Cambridge University Press. Section 1.7.

### Subobject
A subobject of $X$ is an equivalence class of monomorphisms into $X$, where $f: A \to X$ and $g: B \to X$ are equivalent if they factor through each other.

**Reference**: Mac Lane, S. & Moerdijk, I. (1994). *Sheaves in Geometry and Logic*. Universitext. Springer-Verlag. Section I.5.

### Terminal object
An object $1 \in \mathcal{C}$ is terminal if for every object $A$, there exists a unique morphism $A \to 1$.

**Reference**: Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Graduate Texts in Mathematics, vol. 5. Springer-Verlag. Section III.2.

### Universal arrow / universal property
A universal arrow from $c \in \mathcal{C}$ to $G: \mathcal{D} \to \mathcal{C}$ is a pair $(d, \eta: c \to G(d))$ such that for any $f: c \to G(d')$, there exists unique $\bar{f}: d \to d'$ with $G(\bar{f}) \circ \eta = f$.

**Reference**: Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Graduate Texts in Mathematics, vol. 5. Springer-Verlag. Section III.1.

### Weak limit / weak colimit
A weak limit of $F: \mathcal{J} \to \mathcal{C}$ is a cone that satisfies the existence but not uniqueness part of the universal property.

**Reference**: Adámek, J., Herrlich, H., & Strecker, G.E. (1990). *Abstract and Concrete Categories*. John Wiley & Sons. Section 12.

### Zero object
An object that is both initial and terminal.

**Reference**: Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Graduate Texts in Mathematics, vol. 5. Springer-Verlag. Section VIII.2.

### Zero morphism
In a category with zero object $0$, the zero morphism $0_{A,B}: A \to B$ is the composite $A \to 0 \to B$.

**Reference**: Borceux, F. (1994). *Handbook of Categorical Algebra 2: Categories and Structures*. Encyclopedia of Mathematics and its Applications, vol. 51. Cambridge University Press. Section 1.1.

## Basic Higher Category Concepts

### ∗Complicial set
A complicial set is a simplicial set equipped with a marking on each simplex, satisfying compatibility conditions. The marked simplices typically represent "thin" or "degenerate" cells.

**Reference**: Verity, D. (2008). "Complicial sets characterising the simplicial nerves of strict ω-categories". *Memoirs of the American Mathematical Society*, 193(905).

### Cellular set
A cellular set is a presheaf on the category $\Theta$ of finite ordinals with face and degeneracy maps, generalizing simplicial sets.

**Reference**: Makkai, M. & Zawadowski, M. (2001). "The category of 3-computads is not cartesian closed". *Journal of Pure and Applied Algebra*, 160(2-3), 233-240.

### Homotopy category
The homotopy category $\text{Ho}(\mathcal{C})$ of a category with weak equivalences $\mathcal{C}$ is the localization $\mathcal{C}[W^{-1}]$ at the weak equivalences $W$.

**Reference**: Quillen, D.G. (1967). *Homotopical Algebra*. Lecture Notes in Mathematics, vol. 43. Springer-Verlag. Chapter I.

### n-category
An $n$-category has:
- Objects (0-cells)
- 1-morphisms between objects
- 2-morphisms between 1-morphisms
- ...
- $n$-morphisms between $(n-1)$-morphisms
- All $(k>n)$-morphisms are identities

**Reference**: Leinster, T. (2004). *Higher Operads, Higher Categories*. London Mathematical Society Lecture Note Series, vol. 298. Cambridge University Press. Chapter 1.

### ∞-category
An $\infty$-category is a category enriched over $\infty$-groupoids, typically modeled as a quasi-category (Kan-complex-enriched category).

**Reference**: Lurie, J. (2009). *Higher Topos Theory*. Annals of Mathematics Studies, vol. 170. Princeton University Press. Chapter 1.

### Weak n-category
A weak $n$-category has composition and identities satisfying coherence laws only up to higher isomorphisms.

**Reference**: Baez, J.C. & Dolan, J. (1998). "Categorification". In: *Higher Category Theory*, Contemporary Mathematics, vol. 230, pp. 1-36. American Mathematical Society.

### Strict n-category
A strict $n$-category has composition strictly associative and unital at all levels.

**Reference**: Street, R. (1987). "The algebra of oriented simplexes". *Journal of Pure and Applied Algebra*, 49(3), 283-335.

### Bicategory
A bicategory consists of:
- Objects
- 1-morphisms between objects
- 2-morphisms between 1-morphisms
with composition associative and unital up to coherent isomorphism.

**Reference**: Bénabou, J. (1967). "Introduction to bicategories". In: *Reports of the Midwest Category Seminar*, Lecture Notes in Mathematics, vol. 47, pp. 1-77. Springer-Verlag.

### Globular set
A globular set is a presheaf on the globular category $\mathbb{G}$ with objects $[n]$ and parallel source/target maps.

**Reference**: Batanin, M.A. (1998). "Monoidal globular categories as a natural environment for the theory of weak n-categories". *Advances in Mathematics*, 136(1), 39-103.

### Nerve of a category
(See Classical section)

**Reference**: Segal, G. (1974). "Categories and cohomology theories". *Topology*, 13(3), 293-312.

### Quasicategory
A quasicategory is a simplicial set $X$ satisfying the inner horn lifting property: every map $\Lambda^n_i \to X$ ($0 < i < n$) extends to $\Delta^n \to X$.

**Reference**: Joyal, A. (2002). "Quasi-categories and Kan complexes". *Journal of Pure and Applied Algebra*, 175(1-3), 207-222.

### Kan complex
A Kan complex is a simplicial set satisfying all horn lifting properties: every map $\Lambda^n_i \to X$ extends to $\Delta^n \to X$ for all $0 \leq i \leq n$.

**Reference**: Kan, D.M. (1958). "On c.s.s. complexes". *American Journal of Mathematics*, 79(3), 449-476.

### Simplicial set
A simplicial set is a functor $X: \Delta^{op} \to \mathbf{Set}$ from the opposite of the simplex category.

**Reference**: May, J.P. (1967). *Simplicial Objects in Algebraic Topology*. Van Nostrand Mathematical Studies, vol. 11. D. Van Nostrand Company.

### Complete Segal space
A complete Segal space is a Reedy fibrant simplicial space $X: \Delta^{op} \to \mathbf{sSet}$ satisfying:
- Segal condition: $X_n \to X_1 \times_{X_0} \cdots \times_{X_0} X_1$ is a weak equivalence
- Completeness: the map $X_0 \to X_{hoequiv}$ is a weak equivalence

**Reference**: Rezk, C. (2001). "A model for the homotopy theory of homotopy theory". *Transactions of the American Mathematical Society*, 353(3), 973-1007.

### Segal category
A Segal category is a simplicial space satisfying the Segal condition with discrete space of objects $X_0$.

**Reference**: Hirschowitz, A. & Simpson, C. (2001). "Descente pour les n-champs". arXiv:math/9807049.

### Homotopy hypothesis
The homotopy hypothesis asserts that $n$-groupoids model homotopy $n$-types, with $\infty$-groupoids modeling all homotopy types.

**Reference**: Grothendieck, A. (1983). "Pursuing Stacks". Manuscript. Published in: *Documents Mathématiques*, vol. 20 (2022). Société Mathématique de France.

## Types of Higher Categories

### Cartesian closed category
A category $\mathcal{C}$ with finite products such that for each object $A$, the functor $(-) \times A$ has a right adjoint $[A, -]$.

**Reference**: Lambek, J. & Scott, P.J. (1986). *Introduction to Higher Order Categorical Logic*. Cambridge Studies in Advanced Mathematics, vol. 7. Cambridge University Press. Chapter 1.

### Closed category
A symmetric monoidal category where each functor $(-) \otimes A$ has a right adjoint $[A, -]$.

**Reference**: Eilenberg, S. & Kelly, G.M. (1966). "Closed categories". In: *Proceedings of the Conference on Categorical Algebra*, pp. 421-562. Springer-Verlag.

### Compact closed category
A symmetric monoidal category where every object $A$ has a dual $A^*$ with evaluation and coevaluation satisfying the triangle identities.

**Reference**: Kelly, G.M. & Laplaza, M.L. (1980). "Coherence for compact closed categories". *Journal of Pure and Applied Algebra*, 19, 193-213.

### Double category
A double category has:
- Objects
- Horizontal and vertical 1-morphisms
- 2-cells with both horizontal and vertical composition

**Reference**: Ehresmann, C. (1963). "Catégories structurées". *Annales scientifiques de l'École Normale Supérieure*, 80(4), 349-426.

### Enriched category
A $\mathcal{V}$-enriched category has hom-objects $\mathcal{C}(A,B) \in \mathcal{V}$ with composition and identities as morphisms in $\mathcal{V}$.

**Reference**: Kelly, G.M. (1982). *Basic Concepts of Enriched Category Theory*. London Mathematical Society Lecture Note Series, vol. 64. Cambridge University Press. Chapter 1.

### Internal category
An internal category in $\mathcal{E}$ consists of objects $C_0, C_1 \in \mathcal{E}$ with structure maps (source, target, identity, composition) satisfying category axioms internally.

**Reference**: Johnstone, P.T. (2002). *Sketches of an Elephant: A Topos Theory Compendium*. Oxford Logic Guides, vols. 43-44. Oxford University Press. Section B2.1.

### Monoidal category
A category $\mathcal{C}$ with:
- Tensor product $\otimes: \mathcal{C} \times \mathcal{C} \to \mathcal{C}$
- Unit object $I$
- Associativity and unit isomorphisms satisfying coherence conditions

**Reference**: Mac Lane, S. (1963). "Natural associativity and commutativity". *Rice University Studies*, 49(4), 28-46.

### Braided monoidal category
A monoidal category with braiding isomorphism $\beta_{A,B}: A \otimes B \cong B \otimes A$ satisfying the hexagon identities.

**Reference**: Joyal, A. & Street, R. (1993). "Braided tensor categories". *Advances in Mathematics*, 102(1), 20-78.

### Monoidal ∞-category
An $\infty$-category $\mathcal{C}^\otimes \to N(\mathrm{Fin}_*)$ over the nerve of pointed finite sets, encoding a coherent monoidal structure.

**Reference**: Lurie, J. (2017). *Higher Algebra*. Available at: https://www.math.ias.edu/~lurie/papers/HA.pdf. Chapter 2.

### Omega-category (ω-category)
An $\omega$-category has cells of all dimensions $n \geq 0$ with source, target, identity, and composition operations satisfying strict associativity and interchange laws.

**Reference**: Street, R. (1987). "The algebra of oriented simplexes". *Journal of Pure and Applied Algebra*, 49(3), 283-335.

### Pivotal category
A monoidal category with chosen isomorphisms $A \cong A^{**}$ compatible with the monoidal structure.

**Reference**: Barrett, J.W. & Westbury, B.W. (1999). "Spherical categories". *Advances in Mathematics*, 143(2), 357-375.

### Fusion category
A semisimple rigid monoidal category with finitely many simple objects and finite-dimensional hom-spaces.

**Reference**: Etingof, P., Gelaki, S., Nikshych, D., & Ostrik, V. (2015). *Tensor Categories*. Mathematical Surveys and Monographs, vol. 205. American Mathematical Society. Chapter 4.

### Modular tensor category
A ribbon fusion category with non-degenerate braiding (the $S$-matrix is invertible).

**Reference**: Turaev, V. (1994). *Quantum Invariants of Knots and 3-Manifolds*. De Gruyter Studies in Mathematics, vol. 18. Walter de Gruyter. Chapter 2.

### Symmetric monoidal category
A braided monoidal category where $\beta_{B,A} \circ \beta_{A,B} = \text{id}_{A \otimes B}$.

**Reference**: Mac Lane, S. (1963). "Natural associativity and commutativity". *Rice University Studies*, 49(4), 28-46.

### Virtual double category
A double category where horizontal composition is only partially defined, subject to coherence conditions.

**Reference**: Leinster, T. (2002). "Generalized enrichment for categories and multicategories". arXiv:math/0204279.

## Morphisms & Cells

### k-morphism
In an $n$-category, a $k$-morphism is a morphism between $(k-1)$-morphisms for $1 \leq k \leq n$.

**Reference**: Leinster, T. (2004). *Higher Operads, Higher Categories*. London Mathematical Society Lecture Note Series, vol. 298. Cambridge University Press. Section 1.1.

### 2-morphism
A morphism between 1-morphisms in a 2-category or bicategory.

**Reference**: Bénabou, J. (1967). "Introduction to bicategories". In: *Reports of the Midwest Category Seminar*, Lecture Notes in Mathematics, vol. 47, pp. 1-77. Springer-Verlag.

### Higher morphism
Any $k$-morphism for $k > 1$ in a higher category.

**Reference**: Street, R. (1996). "Categorical structures". In: *Handbook of Algebra*, vol. 1, pp. 529-577. North-Holland.

### Globular k-cell
A $k$-dimensional cell in a globular set with source and target $(k-1)$-cells.

**Reference**: Batanin, M.A. (1998). "Monoidal globular categories as a natural environment for the theory of weak n-categories". *Advances in Mathematics*, 136(1), 39-103.

### Icon
A 2-morphism in a double category filling a square of 1-morphisms.

**Reference**: Dawson, R., Paré, R., & Pronk, D. (2004). "Paths in double categories". *Theory and Applications of Categories*, 16(18), 460-521.

### Lax natural transformation
For 2-functors $F, G: \mathcal{C} \to \mathcal{D}$, a lax natural transformation has components $\alpha_c: F(c) \to G(c)$ and 2-cells $\alpha_f: G(f) \circ \alpha_c \Rightarrow \alpha_{c'} \circ F(f)$ satisfying coherence.

**Reference**: Street, R. (1972). "Two constructions on lax functors". *Cahiers de Topologie et Géométrie Différentielle Catégoriques*, 13(3), 217-264.

### Oplax natural transformation
Dual to lax: 2-cells go $\alpha_f: \alpha_{c'} \circ F(f) \Rightarrow G(f) \circ \alpha_c$.

**Reference**: Lack, S. (2010). "Icons". *Applied Categorical Structures*, 18(3), 289-307.

### Pseudonatural transformation
A lax natural transformation where all 2-cells $\alpha_f$ are isomorphisms.

**Reference**: Gray, J.W. (1974). *Formal Category Theory: Adjointness for 2-Categories*. Lecture Notes in Mathematics, vol. 391. Springer-Verlag.

### Modification
A modification between natural transformations $\alpha, \beta: F \Rightarrow G$ assigns to each object $c$ a 2-morphism $\Gamma_c: \alpha_c \Rightarrow \beta_c$ satisfying naturality.

**Reference**: Street, R. (1987). "Correction to 'Fibrations in bicategories'". *Cahiers de Topologie et Géométrie Différentielle Catégoriques*, 28(1), 53-56.

### Equivalence in higher categories
A morphism with a quasi-inverse up to coherent higher isomorphisms. In an $(\infty,1)$-category, an equivalence is a morphism that becomes an isomorphism in the homotopy category.

**Reference**: Lurie, J. (2009). *Higher Topos Theory*. Annals of Mathematics Studies, vol. 170. Princeton University Press. Section 1.2.10.

### Adjoint equivalence
An equivalence realized by an adjunction where unit and counit are isomorphisms.

**Reference**: Blackwell, R., Kelly, G.M., & Power, A.J. (1989). "Two-dimensional monad theory". *Journal of Pure and Applied Algebra*, 59(1), 1-41.

## Functors & Transformations

### ∞-functor
A map of simplicial sets $F: \mathcal{C} \to \mathcal{D}$ between quasi-categories preserving composition up to homotopy.

**Reference**: Lurie, J. (2009). *Higher Topos Theory*. Annals of Mathematics Studies, vol. 170. Princeton University Press. Section 1.2.7.

### Functor between bicategories
A (pseudo)functor $F: \mathcal{B} \to \mathcal{B}'$ preserving composition and identities up to coherent 2-isomorphism.

**Reference**: Bénabou, J. (1967). "Introduction to bicategories". In: *Reports of the Midwest Category Seminar*, Lecture Notes in Mathematics, vol. 47, pp. 1-77. Springer-Verlag.

### Homotopy coherent diagram
A functor from a simplicial category to an $\infty$-category, encoding coherent homotopies between composites.

**Reference**: Cordier, J.M. & Porter, T. (1986). "Vogt's theorem on categories of homotopy coherent diagrams". *Mathematical Proceedings of the Cambridge Philosophical Society*, 100(1), 65-90.

### Lax functor
A functor between bicategories with coherence 2-cells $F(g \circ f) \Rightarrow F(g) \circ F(f)$ and $1_{F(A)} \Rightarrow F(1_A)$.

**Reference**: Street, R. (1972). "Two constructions on lax functors". *Cahiers de Topologie et Géométrie Différentielle Catégoriques*, 13(3), 217-264.

### Oplax functor
Dual: coherence 2-cells $F(g) \circ F(f) \Rightarrow F(g \circ f)$ and $F(1_A) \Rightarrow 1_{F(A)}$.

**Reference**: Street, R. (1980). "Fibrations in bicategories". *Cahiers de Topologie et Géométrie Différentielle Catégoriques*, 21(2), 111-160.

### Pseudofunctor
A lax functor where all coherence 2-cells are isomorphisms.

**Reference**: Gray, J.W. (1974). *Formal Category Theory: Adjointness for 2-Categories*. Lecture Notes in Mathematics, vol. 391. Springer-Verlag.

### Transformation between ∞-functors
A homotopy between maps of quasi-categories, represented by a map $\mathcal{C} \times \Delta^1 \to \mathcal{D}$.

**Reference**: Lurie, J. (2009). *Higher Topos Theory*. Annals of Mathematics Studies, vol. 170. Princeton University Press. Section 1.2.7.

### Natural isomorphism up to higher equivalence
In an $n$-category, a natural transformation whose components are equivalences.

**Reference**: Leinster, T. (2004). *Higher Operads, Higher Categories*. London Mathematical Society Lecture Note Series, vol. 298. Cambridge University Press. Chapter 5.

## Limits & Colimits

### Homotopy colimit
The derived functor of the colimit functor, computed by replacing the diagram with a cofibrant resolution.

**Reference**: Bousfield, A.K. & Kan, D.M. (1972). *Homotopy Limits, Completions and Localizations*. Lecture Notes in Mathematics, vol. 304. Springer-Verlag. Chapter XI.

### Homotopy limit
The derived functor of the limit functor, computed using fibrant resolutions.

**Reference**: Bousfield, A.K. & Kan, D.M. (1972). *Homotopy Limits, Completions and Localizations*. Lecture Notes in Mathematics, vol. 304. Springer-Verlag. Chapter XI.

### ∞-categorical colimit
A colimit in an $\infty$-category, representing the initial object of the $\infty$-category of cocones.

**Reference**: Lurie, J. (2009). *Higher Topos Theory*. Annals of Mathematics Studies, vol. 170. Princeton University Press. Section 1.2.13.

### ∞-categorical limit
Dual: the terminal object in the $\infty$-category of cones.

**Reference**: Lurie, J. (2009). *Higher Topos Theory*. Annals of Mathematics Studies, vol. 170. Princeton University Press. Section 1.2.13.

### Weighted limit
The limit of $J: \mathcal{C} \to \mathcal{D}$ weighted by $W: \mathcal{C}^{op} \to \mathbf{Set}$ is the representation of the functor $d \mapsto [\mathcal{C}, \mathbf{Set}](W, \mathcal{D}(d, J-))$.

**Reference**: Kelly, G.M. (1982). *Basic Concepts of Enriched Category Theory*. London Mathematical Society Lecture Note Series, vol. 64. Cambridge University Press. Section 3.1.

### Bicolimit
A 2-categorical colimit, defined up to equivalence rather than isomorphism.

**Reference**: Street, R. (1980). "Fibrations in bicategories". *Cahiers de Topologie et Géométrie Différentielle Catégoriques*, 21(2), 111-160.

### Flexible limit
A limit in a 2-category where the universal property holds up to isomorphism rather than equality.

**Reference**: Bird, G., Kelly, G.M., Power, A.J., & Street, R. (1989). "Flexible limits for 2-categories". *Journal of Pure and Applied Algebra*, 61(1), 1-27.

### Kan extension in higher categories
The $\infty$-categorical generalization where the universal property holds up to contractible space of choices.

**Reference**: Lurie, J. (2009). *Higher Topos Theory*. Annals of Mathematics Studies, vol. 170. Princeton University Press. Section 4.3.

### Lax limit
A weak 2-limit where the universal property provides existence but not uniqueness.

**Reference**: Street, R. (1976). "Limits indexed by category-valued 2-functors". *Journal of Pure and Applied Algebra*, 8(2), 149-181.

### Pseudolimit
A 2-limit where factorizations are unique up to unique isomorphism.

**Reference**: Street, R. (1976). "Limits indexed by category-valued 2-functors". *Journal of Pure and Applied Algebra*, 8(2), 149-181.

### End
(See Classical section)

**Reference**: Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Graduate Texts in Mathematics, vol. 5. Springer-Verlag. Section IX.5.

### Bilimit
A 2-categorical limit, dual to bicolimit.

**Reference**: Street, R. (1980). "Fibrations in bicategories". *Cahiers de Topologie et Géométrie Différentielle Catégoriques*, 21(2), 111-160.

## Adjunctions & Duality

### Adjunction in bicategories
1-morphisms $L: A \to B$ and $R: B \to A$ with 2-morphisms $\eta: 1_A \Rightarrow R \circ L$ and $\epsilon: L \circ R \Rightarrow 1_B$ satisfying triangle identities up to coherent modification.

**Reference**: Street, R. (1980). "Fibrations in bicategories". *Cahiers de Topologie et Géométrie Différentielle Catégoriques*, 21(2), 111-160.

### Biadjunction
An adjunction in a bicategory where the triangle identities hold up to invertible modifications.

**Reference**: Lack, S. (2000). "A coherent approach to pseudomonads". *Advances in Mathematics*, 152(2), 179-202.

### Lax adjunction
An adjunction where one or both triangle identities hold only laxly.

**Reference**: Gray, J.W. (1974). *Formal Category Theory: Adjointness for 2-Categories*. Lecture Notes in Mathematics, vol. 391. Springer-Verlag.

### ∞-adjunction
An adjunction in an $\infty$-category, characterized by the mapping spaces $\text{Map}(L(x), y) \simeq \text{Map}(x, R(y))$ being equivalent.

**Reference**: Lurie, J. (2009). *Higher Topos Theory*. Annals of Mathematics Studies, vol. 170. Princeton University Press. Section 5.2.2.

### Coend calculus
The calculus of coends, using the universal property to manipulate expressions involving $\int^c F(c,c)$.

**Reference**: Loregian, F. (2021). *(Co)end Calculus*. London Mathematical Society Lecture Note Series, vol. 468. Cambridge University Press.

### Dualizable object
In a monoidal category, an object $A$ with dual $A^*$ and evaluation/coevaluation maps satisfying the triangle identities.

**Reference**: Dold, A. & Puppe, D. (1980). "Duality, trace, and transfer". *Proceedings of the International Conference on Geometric Topology*, pp. 81-102.

### Fully dualizable object
In a monoidal $n$-category, an object with duals at all levels up to dimension $n$.

**Reference**: Lurie, J. (2009). "On the classification of topological field theories". *Current Developments in Mathematics*, 2008, 129-280.

### Serre duality
In a triangulated category, a contravariant equivalence $D: \mathcal{C}^{op} \to \mathcal{C}$ with natural isomorphisms $\text{Hom}(X,Y) \cong \text{Hom}(Y,DX)^*$.

**Reference**: Serre, J.P. (1955). "Un théorème de dualité". *Commentarii Mathematici Helvetici*, 29, 9-26.

### Verdier duality
The duality on the derived category of sheaves given by $\mathbb{D}(F) = R\mathcal{H}om(F, \omega_X)$ for dualizing complex $\omega_X$.

**Reference**: Verdier, J.L. (1967). "Dualité dans la cohomologie des espaces localement compacts". *Séminaire Bourbaki*, 300, 337-349.

### Grothendieck duality
For proper morphism $f: X \to Y$, the isomorphism $Rf_* R\mathcal{H}om(F, f^!\mathcal{O}_Y) \cong R\mathcal{H}om(Rf_*F, \mathcal{O}_Y)$.

**Reference**: Hartshorne, R. (1966). *Residues and Duality*. Lecture Notes in Mathematics, vol. 20. Springer-Verlag.

## Monads & Algebras

### Monad in a bicategory
An endomorphism $T: A \to A$ with 2-morphisms $\mu: T \circ T \Rightarrow T$ and $\eta: 1_A \Rightarrow T$ satisfying associativity and unit laws.

**Reference**: Street, R. (1972). "The formal theory of monads". *Journal of Pure and Applied Algebra*, 2(2), 149-168.

### Comonad
Dual: an endomorphism with comultiplication $\delta: T \Rightarrow T \circ T$ and counit $\epsilon: T \Rightarrow 1_A$.

**Reference**: Huber, P.J. (1961). "Homotopy theory in general categories". *Mathematische Annalen*, 144(5), 361-385.

### Eilenberg–Moore object
The object of algebras for a monad, when it exists in the ambient bicategory.

**Reference**: Eilenberg, S. & Moore, J.C. (1965). "Adjoint functors and triples". *Illinois Journal of Mathematics*, 9(3), 381-398.

### Kleisli object
The free algebras for a monad, representing the initial way to resolve the monad.

**Reference**: Kleisli, H. (1965). "Every standard construction is induced by a pair of adjoint functors". *Proceedings of the American Mathematical Society*, 16(3), 544-546.

### Distributive law
A 2-morphism $\lambda: S \circ T \Rightarrow T \circ S$ between monads satisfying compatibility with their structures.

**Reference**: Beck, J. (1969). "Distributive laws". In: *Seminar on Triples and Categorical Homology Theory*, Lecture Notes in Mathematics, vol. 80, pp. 119-140. Springer-Verlag.

### Algebras for a monad
An algebra for monad $(T, \mu, \eta)$ is an object $A$ with structure map $\alpha: T(A) \to A$ satisfying $\alpha \circ \mu_A = \alpha \circ T(\alpha)$ and $\alpha \circ \eta_A = \text{id}_A$.

**Reference**: Eilenberg, S. & Moore, J.C. (1965). "Adjoint functors and triples". *Illinois Journal of Mathematics*, 9(3), 381-398.

### Coalgebras
Dual: an object $C$ with $\gamma: C \to T(C)$ satisfying coassociativity and counit conditions.

**Reference**: Barr, M. (1970). "Coalgebras over a commutative ring". *Journal of Algebra*, 15(1), 1-40.

### Monadic functor
A functor $U: \mathcal{B} \to \mathcal{A}$ that has a left adjoint and exhibits $\mathcal{B}$ as equivalent to the category of algebras for the induced monad.

**Reference**: Beck, J. (1967). "Triples, algebras and cohomology". PhD thesis, Columbia University. Reprinted in: *Theory and Applications of Categories*, 2 (2003), 1-59.

### Barr–Beck theorem
$U: \mathcal{B} \to \mathcal{A}$ is monadic if and only if:
- $U$ has a left adjoint
- $U$ reflects isomorphisms
- $\mathcal{B}$ has coequalizers of $U$-split pairs and $U$ preserves them

**Reference**: Barr, M. & Beck, J. (1969). "Homology and standard constructions". In: *Seminar on Triples and Categorical Homology Theory*, Lecture Notes in Mathematics, vol. 80, pp. 245-335. Springer-Verlag.

### Lax algebra
For a 2-monad $T$, a lax algebra has structure 2-morphism $\alpha: T(A) \to A$ satisfying laws up to coherent 2-cells.

**Reference**: Lack, S. (2000). "A coherent approach to pseudomonads". *Advances in Mathematics*, 152(2), 179-202.

### Pseudo-monad
A monad in a bicategory where associativity and unit laws hold up to coherent isomorphism.

**Reference**: Marmolejo, F. (1999). "Distributive laws for pseudomonads". *Theory and Applications of Categories*, 5(5), 91-147.

### Pseudo-algebra
An algebra for a pseudo-monad where the algebra laws hold up to coherent isomorphism.

**Reference**: Blackwell, R., Kelly, G.M., & Power, A.J. (1989). "Two-dimensional monad theory". *Journal of Pure and Applied Algebra*, 59(1), 1-41.

## Operads & Algebraic Structures

### Operad
An operad $\mathcal{P}$ consists of:
- Objects $\mathcal{P}(n)$ of $n$-ary operations for each $n \geq 0$
- Composition maps $\gamma: \mathcal{P}(k) \times \mathcal{P}(n_1) \times \cdots \times \mathcal{P}(n_k) \to \mathcal{P}(n_1 + \cdots + n_k)$
- Unit $1 \in \mathcal{P}(1)$
- $\Sigma_n$-action on $\mathcal{P}(n)$
satisfying associativity, unit, and equivariance axioms.

**Reference**: May, J.P. (1972). *The Geometry of Iterated Loop Spaces*. Lecture Notes in Mathematics, vol. 271. Springer-Verlag.

### Multicategory
(See Classical section)

**Reference**: Leinster, T. (2004). *Higher Operads, Higher Categories*. London Mathematical Society Lecture Note Series, vol. 298. Cambridge University Press. Chapter 2.

### PROP
A PROP (product and permutation category) is a symmetric monoidal category whose objects are natural numbers with monoidal product given by addition.

**Reference**: Mac Lane, S. (1965). "Categorical algebra". *Bulletin of the American Mathematical Society*, 71(1), 40-106.

### Lawvere theory
(See Classical section)

**Reference**: Lawvere, F.W. (1963). "Functorial semantics of algebraic theories". *Proceedings of the National Academy of Sciences*, 50(5), 869-872.

### Topological operad
An operad enriched in topological spaces, with continuous composition maps.

**Reference**: May, J.P. (1972). *The Geometry of Iterated Loop Spaces*. Lecture Notes in Mathematics, vol. 271. Springer-Verlag.

### Symmetric operad
An operad in the category of $\mathbb{S}$-modules, where $\mathbb{S}$ is the groupoid of finite sets and bijections.

**Reference**: Elmendorf, A.D. & Mandell, M.A. (2004). "Rings, modules, and algebras in infinite loop space theory". *Advances in Mathematics*, 205(1), 163-228.

### Cyclic operad
An operad with additional $S_{n+1}$-action on $\mathcal{P}(n)$ compatible with composition, encoding operations with no distinguished output.

**Reference**: Getzler, E. & Kapranov, M.M. (1995). "Cyclic operads and cyclic homology". In: *Geometry, Topology, & Physics*, pp. 167-201. International Press.

### Modular operad
An operad with operations labeled by genus and allowing self-gluings, used in the study of moduli spaces of curves.

**Reference**: Getzler, E. & Kapranov, M.M. (1998). "Modular operads". *Compositio Mathematica*, 110(1), 65-126.

### Algebra over an operad
For an operad $\mathcal{P}$, a $\mathcal{P}$-algebra is an object $A$ with structure maps $\mathcal{P}(n) \otimes A^{\otimes n} \to A$ satisfying associativity and unit conditions.

**Reference**: May, J.P. (1972). *The Geometry of Iterated Loop Spaces*. Lecture Notes in Mathematics, vol. 271. Springer-Verlag.

### Coalgebra over an operad
Dual: structure maps $C \to \mathcal{P}(n) \otimes C^{\otimes n}$ satisfying coassociativity.

**Reference**: Ching, M. (2005). "Bar constructions for topological operads and the Goodwillie derivatives of the identity". *Geometry & Topology*, 9, 833-933.

### ∞-operad
A fibration $\mathcal{O}^\otimes \to N(\mathrm{Fin}_*)$ of simplicial sets satisfying Segal conditions, encoding coherent operadic composition.

**Reference**: Lurie, J. (2017). *Higher Algebra*. Available at: https://www.math.ias.edu/~lurie/papers/HA.pdf. Chapter 2.

### Dendroidal set
A presheaf on the category $\Omega$ of trees, generalizing simplicial sets to encode operadic structures.

**Reference**: Moerdijk, I. & Weiss, I. (2007). "Dendroidal sets". *Algebraic & Geometric Topology*, 7, 1441-1470.

### Colored operad
An operad with multiple sorts, having operations $\mathcal{P}(c_1,\ldots,c_n;c)$ with typed inputs and output.

**Reference**: Berger, C. & Moerdijk, I. (2003). "Axiomatic homotopy theory for operads". *Commentarii Mathematici Helvetici*, 78(4), 805-831.

### Properad
A generalization of operads allowing operations with multiple inputs and outputs, encoded as directed graphs.

**Reference**: Vallette, B. (2007). "A Koszul duality for props". *Transactions of the American Mathematical Society*, 359(10), 4865-4943.

### ∞-properad
The $\infty$-categorical version, typically modeled using presheaves on graphs with appropriate Segal conditions.

**Reference**: Hackney, P., Robertson, M., & Yau, D. (2015). "Infinity properads and infinity wheeled properads". Lecture Notes in Mathematics, vol. 2147. Springer.

## Topology & Homotopy Theory

### Classifying space
For a group $G$, the classifying space $BG$ has $\pi_1(BG) = G$ and contractible universal cover $EG$.

**Reference**: Milnor, J. (1956). "Construction of universal bundles, II". *Annals of Mathematics*, 63(3), 430-436.

### Delooping
For a pointed space $X$, a delooping is a space $BX$ with $\Omega BX \simeq X$.

**Reference**: May, J.P. (1972). *The Geometry of Iterated Loop Spaces*. Lecture Notes in Mathematics, vol. 271. Springer-Verlag.

### Loop space
The space $\Omega X = \text{Map}_*((S^1,*),(X,*))$ of based loops in $X$.

**Reference**: Adams, J.F. (1978). *Infinite Loop Spaces*. Annals of Mathematics Studies, vol. 90. Princeton University Press.

### Loop space object
In an $\infty$-category, the pullback of $* \to X \leftarrow *$.

**Reference**: Lurie, J. (2009). *Higher Topos Theory*. Annals of Mathematics Studies, vol. 170. Princeton University Press. Section 1.2.2.

### Mapping space
In an $\infty$-category $\mathcal{C}$, the space $\text{Map}_\mathcal{C}(X,Y)$ of morphisms from $X$ to $Y$.

**Reference**: Lurie, J. (2009). *Higher Topos Theory*. Annals of Mathematics Studies, vol. 170. Princeton University Press. Section 1.2.2.

### Fundamental ∞-groupoid
The $\infty$-groupoid $\Pi_\infty(X)$ with points as objects and paths up to higher homotopies as morphisms.

**Reference**: Grothendieck, A. (1983). "Pursuing Stacks". Manuscript. Published in: *Documents Mathématiques*, vol. 20 (2022). Société Mathématique de France.

### Homotopy fiber
For $f: X \to Y$, the homotopy fiber over $y \in Y$ is the pullback of $f$ along $y: * \to Y$ in the $\infty$-category of spaces.

**Reference**: May, J.P. (1999). *A Concise Course in Algebraic Topology*. Chicago Lectures in Mathematics. University of Chicago Press. Chapter 8.

### Homotopy n-type
A space $X$ with $\pi_k(X) = 0$ for all $k > n$.

**Reference**: Whitehead, G.W. (1978). *Elements of Homotopy Theory*. Graduate Texts in Mathematics, vol. 61. Springer-Verlag. Chapter 4.

### Homotopy quotient
For $G$ acting on $X$, the homotopy quotient is $X \times_G EG = (X \times EG)/G$.

**Reference**: tom Dieck, T. (1987). *Transformation Groups*. De Gruyter Studies in Mathematics, vol. 8. Walter de Gruyter. Chapter 7.

### Stabilization
The process of passing from pointed spaces to spectra by iterating the loop-suspension adjunction.

**Reference**: Adams, J.F. (1974). *Stable Homotopy and Generalised Homology*. Chicago Lectures in Mathematics. University of Chicago Press.

### Suspension
The suspension $\Sigma X = X \wedge S^1$ with adjunction $[\Sigma X, Y] \cong [X, \Omega Y]$.

**Reference**: Hatcher, A. (2002). *Algebraic Topology*. Cambridge University Press. Section 4.1.

## Model Structures

### Model category
A category $\mathcal{C}$ with three distinguished classes of morphisms:
- Weak equivalences $W$
- Fibrations $F$
- Cofibrations $C$
satisfying axioms including: existence of limits/colimits, 2-out-of-3, retracts, lifting, and factorization.

**Reference**: Quillen, D.G. (1967). *Homotopical Algebra*. Lecture Notes in Mathematics, vol. 43. Springer-Verlag.

### Simplicial model category
A model category enriched over simplicial sets compatibly with the model structure.

**Reference**: Quillen, D.G. (1967). *Homotopical Algebra*. Lecture Notes in Mathematics, vol. 43. Springer-Verlag. Chapter II.

### Quillen adjunction
An adjunction $L: \mathcal{C} \rightleftarrows \mathcal{D} : R$ where $L$ preserves cofibrations and acyclic cofibrations (equivalently, $R$ preserves fibrations and acyclic fibrations).

**Reference**: Quillen, D.G. (1967). *Homotopical Algebra*. Lecture Notes in Mathematics, vol. 43. Springer-Verlag. Section I.4.

### Quillen equivalence
A Quillen adjunction inducing an equivalence of homotopy categories $\text{Ho}(\mathcal{C}) \simeq \text{Ho}(\mathcal{D})$.

**Reference**: Hovey, M. (1999). *Model Categories*. Mathematical Surveys and Monographs, vol. 63. American Mathematical Society. Section 1.3.

### Fibration in model categories
A morphism in the class $F$, characterized by the right lifting property against acyclic cofibrations.

**Reference**: Hirschhorn, P.S. (2003). *Model Categories and Their Localizations*. Mathematical Surveys and Monographs, vol. 99. American Mathematical Society. Section 7.1.

### Cofibration
A morphism in the class $C$, characterized by the left lifting property against acyclic fibrations.

**Reference**: Hirschhorn, P.S. (2003). *Model Categories and Their Localizations*. Mathematical Surveys and Monographs, vol. 99. American Mathematical Society. Section 7.1.

### Weak equivalence
A morphism in the class $W$, becoming an isomorphism in the homotopy category.

**Reference**: Dwyer, W.G. & Spalinski, J. (1995). "Homotopy theories and model categories". In: *Handbook of Algebraic Topology*, pp. 73-126. North-Holland.

### Left Bousfield localization
For a model category $\mathcal{C}$ and set $S$ of morphisms, the left Bousfield localization has:
- Same cofibrations
- Weak equivalences = $S$-local equivalences
- Fibrations determined by lifting

**Reference**: Bousfield, A.K. (1975). "The localization of spaces with respect to homology". *Topology*, 14(2), 133-150.

### Right Bousfield localization
Dual: keeps the same fibrations and localizes the weak equivalences.

**Reference**: Hirschhorn, P.S. (2003). *Model Categories and Their Localizations*. Mathematical Surveys and Monographs, vol. 99. American Mathematical Society. Chapter 5.

### Monoidal model category
A model category with monoidal structure such that:
- Tensor product of cofibrations is a cofibration
- Pushout-product axiom holds

**Reference**: Hovey, M. (1999). *Model Categories*. Mathematical Surveys and Monographs, vol. 63. American Mathematical Society. Section 4.2.

### Enriched model category
A model category enriched over a monoidal model category $\mathcal{V}$ with compatible enriched lifting properties.

**Reference**: Barwick, C. (2010). "On left and right model categories and left and right Bousfield localizations". *Homology, Homotopy and Applications*, 12(2), 245-320.

### Relative category
A category $\mathcal{C}$ with a distinguished class $W$ of weak equivalences.

**Reference**: Dwyer, W.G. & Kan, D.M. (1980). "Calculating simplicial localizations". *Journal of Pure and Applied Algebra*, 18(1), 17-35.

## Advanced Constructions

### Yoneda embedding for ∞-categories
The fully faithful functor $\mathcal{C} \to \text{Fun}(\mathcal{C}^{op}, \mathcal{S})$ into presheaves of spaces.

**Reference**: Lurie, J. (2009). *Higher Topos Theory*. Annals of Mathematics Studies, vol. 170. Princeton University Press. Section 5.1.3.

### Grothendieck construction
For $F: \mathcal{C} \to \mathbf{Cat}$, the category $\int F$ with objects $(c, x \in F(c))$ and morphisms respecting the functoriality.

**Reference**: Grothendieck, A. (1971). *Revêtements étales et groupe fondamental (SGA 1)*. Lecture Notes in Mathematics, vol. 224. Springer-Verlag. Exposé VI.

### Straightening and unstraightening
The equivalence between fibrations $\mathcal{E} \to \mathcal{C}$ and functors $\mathcal{C} \to \mathbf{Cat}$ (or their $\infty$-categorical versions).

**Reference**: Lurie, J. (2009). *Higher Topos Theory*. Annals of Mathematics Studies, vol. 170. Princeton University Press. Section 3.2.

### Factorization system
(See Classical section)

**Reference**: Freyd, P.J. & Kelly, G.M. (1972). "Categories of continuous functors, I". *Journal of Pure and Applied Algebra*, 2(3), 169-191.

### Orthogonal factorization system
A factorization system $(\mathcal{E}, \mathcal{M})$ where $\mathcal{E}$ and $\mathcal{M}$ are characterized by mutual orthogonality (unique lifting).

**Reference**: Riehl, E. (2011). "Algebraic model structures". *New York Journal of Mathematics*, 17, 173-231.

### Reflective subcategory
(See Classical section)

**Reference**: Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Graduate Texts in Mathematics, vol. 5. Springer-Verlag. Section IV.3.

### Coreflective subcategory
(See Classical section)

**Reference**: Adámek, J. & Rosický, J. (1994). *Locally Presentable and Accessible Categories*. London Mathematical Society Lecture Note Series, vol. 189. Cambridge University Press. Section 1.36.

### Exact ∞-category
An $\infty$-category with a notion of exact sequences, typically a stable $\infty$-category with a t-structure.

**Reference**: Barwick, C. (2015). "On exact infinity-categories and the theorem of the heart". *Compositio Mathematica*, 151(11), 2160-2186.

### Stable ∞-category
An $\infty$-category where:
- Finite limits and colimits exist
- Initial and terminal objects coincide
- Squares are pullbacks iff they are pushouts

**Reference**: Lurie, J. (2017). *Higher Algebra*. Available at: https://www.math.ias.edu/~lurie/papers/HA.pdf. Chapter 1.

### Presentable ∞-category
An $\infty$-category equivalent to the localization of a presheaf $\infty$-category at a small set of morphisms.

**Reference**: Lurie, J. (2009). *Higher Topos Theory*. Annals of Mathematics Studies, vol. 170. Princeton University Press. Section 5.5.0.

### Accessible ∞-category
An $\infty$-category with $\kappa$-compact objects generating under $\kappa$-filtered colimits.

**Reference**: Lurie, J. (2009). *Higher Topos Theory*. Annals of Mathematics Studies, vol. 170. Princeton University Press. Section 5.4.

### Topos
A category equivalent to the category of sheaves on some site, characterized by having finite limits, exponentials, and subobject classifier.

**Reference**: Johnstone, P.T. (2002). *Sketches of an Elephant: A Topos Theory Compendium*. Oxford Logic Guides, vols. 43-44. Oxford University Press.

### Higher topos
An $\infty$-category satisfying the $\infty$-categorical version of Giraud's axioms.

**Reference**: Lurie, J. (2009). *Higher Topos Theory*. Annals of Mathematics Studies, vol. 170. Princeton University Press. Section 6.1.

### (∞,1)-topos
An $\infty$-topos where all $n$-morphisms for $n > 1$ are invertible.

**Reference**: Lurie, J. (2009). *Higher Topos Theory*. Annals of Mathematics Studies, vol. 170. Princeton University Press. Definition 6.1.0.4.

### (∞,n)-category
An $\infty$-category where all $k$-morphisms for $k > n$ are invertible.

**Reference**: Barwick, C. & Schommer-Pries, C. (2011). "On the unicity of the homotopy theory of higher categories". arXiv:1112.0040.

### Cobordism hypothesis
The statement that the $(\infty,n)$-category of fully dualizable objects in a symmetric monoidal $(\infty,n)$-category $\mathcal{C}$ is equivalent to $\text{Bord}_n$ evaluated at $\mathcal{C}$.

**Reference**: Baez, J.C. & Dolan, J. (1995). "Higher-dimensional algebra and topological quantum field theory". *Journal of Mathematical Physics*, 36(11), 6073-6105.

### Day convolution
For functors $F, G: \mathcal{C} \to \mathcal{V}$ where $\mathcal{C}$ is monoidal, the Day convolution is:
$$F \star G = \int^{c,d \in \mathcal{C}} F(c) \otimes G(d) \otimes \mathcal{C}(-, c \otimes d)$$

**Reference**: Day, B. (1970). "On closed categories of functors". In: *Reports of the Midwest Category Seminar IV*, Lecture Notes in Mathematics, vol. 137, pp. 1-38. Springer-Verlag.

### Tannaka duality
The reconstruction of a group (or Hopf algebra) from its category of representations with forgetful functor.

**Reference**: Deligne, P. & Milne, J.S. (1982). "Tannakian categories". In: *Hodge Cycles, Motives, and Shimura Varieties*, Lecture Notes in Mathematics, vol. 900, pp. 101-228. Springer-Verlag.

### Twisted arrow category
The category $\text{Tw}(\mathcal{C})$ with objects being morphisms of $\mathcal{C}$ and morphisms $(f: a \to b) \to (g: c \to d)$ being commutative squares.

**Reference**: Mac Lane, S. & Paré, R. (1985). "Coherence for bicategories and indexed categories". *Journal of Pure and Applied Algebra*, 37, 59-80.

## Dimensional Enhancements

### 2-category
A category enriched over $\mathbf{Cat}$, having objects, 1-morphisms, and 2-morphisms with strict composition.

**Reference**: Kelly, G.M. & Street, R. (1974). "Review of the elements of 2-categories". In: *Category Seminar*, Lecture Notes in Mathematics, vol. 420, pp. 75-103. Springer-Verlag.

### 3-category
A category with objects, 1-morphisms, 2-morphisms, and 3-morphisms, with composition strict at all levels.

**Reference**: Gordon, R., Power, A.J., & Street, R. (1995). "Coherence for tricategories". *Memoirs of the American Mathematical Society*, 117(558).

### n-fold category
An $n$-fold category has $n$ different directions of morphisms, generalizing double categories.

**Reference**: Ehresmann, C. (1963). "Catégories structurées". *Annales scientifiques de l'École Normale Supérieure*, 80(4), 349-426.

### Iterated span category
The $n$-fold category $\text{Span}_n(\mathcal{C})$ with $n$ levels of spans in $\mathcal{C}$.

**Reference**: Haugseng, R. (2018). "Iterated spans and classical topological field theories". *Mathematische Zeitschrift*, 289(3-4), 1427-1488.

### Gray-category
A category enriched over Gray's tensor product of 2-categories, giving a semi-strict 3-category.

**Reference**: Gray, J.W. (1974). *Formal Category Theory: Adjointness for 2-Categories*. Lecture Notes in Mathematics, vol. 391. Springer-Verlag.

### Trimble n-category
An iterative definition where an $n$-category is a category enriched over $(n-1)$-categories with appropriate coherence.

**Reference**: Cheng, E. & Gurski, N. (2011). "The periodic table of n-categories for low dimensions I: degenerate categories and degenerate bicategories". In: *Categories in Algebra, Geometry and Mathematical Physics*, Contemporary Mathematics, vol. 431, pp. 143-164.

### Tamsamani n-category
A simplicial object in $(n-1)$-categories satisfying the Segal condition at each level.

**Reference**: Tamsamani, Z. (1999). "Sur des notions de n-catégorie et n-groupoïde non strictes via des ensembles multi-simpliciaux". *K-Theory*, 16(1), 51-99.

### Street nerve
The nerve construction taking a bicategory to a simplicial category encoding its structure.

**Reference**: Street, R. (1987). "The algebra of oriented simplexes". *Journal of Pure and Applied Algebra*, 49(3), 283-335.

### Θ-space
A presheaf on Joyal's category $\Theta$ satisfying Segal conditions, modeling $(\infty,n)$-categories.

**Reference**: Rezk, C. (2010). "A cartesian presentation of weak n-categories". *Geometry & Topology*, 14(1), 521-571.

### Rezk completion
The fibrant replacement in the complete Segal space model structure, forcing essential surjectivity.

**Reference**: Rezk, C. (2001). "A model for the homotopy theory of homotopy theory". *Transactions of the American Mathematical Society*, 353(3), 973-1007.

### Homotopy coherent nerve
The nerve functor from simplicial categories to simplicial sets, preserving the homotopy theory.

**Reference**: Cordier, J.M. (1982). "Sur la notion de diagramme homotopiquement cohérent". *Cahiers de Topologie et Géométrie Différentielle Catégoriques*, 23(1), 93-112.

### ω-category
(See Types of Higher Categories)

**Reference**: Street, R. (1987). "The algebra of oriented simplexes". *Journal of Pure and Applied Algebra*, 49(3), 283-335.

## Algebraic Geometry & Physics

### Derived stack
An $\infty$-functor $\mathcal{X}: \text{CAlg}^{op} \to \mathcal{S}$ from commutative algebras to spaces, satisfying descent for étale covers.

**Reference**: Toën, B. & Vezzosi, G. (2008). "Homotopical algebraic geometry II: Geometric stacks and applications". *Memoirs of the American Mathematical Society*, 193(902).

### Higher stack
An $n$-stack is a presheaf of $(n-1)$-groupoids satisfying descent.

**Reference**: Simpson, C. (1996). "Algebraic (geometric) n-stacks". arXiv:alg-geom/9609014.

### Perfect stack
A derived stack whose cotangent complex has perfect amplitude in a specified range.

**Reference**: Toën, B. & Vezzosi, G. (2008). "Homotopical algebraic geometry II: Geometric stacks and applications". *Memoirs of the American Mathematical Society*, 193(902).

### Geometric Langlands program
The correspondence between $D$-modules on $\text{Bun}_G$ and quasi-coherent sheaves on $\text{Loc}_{G^\vee}$.

**Reference**: Frenkel, E. (2007). "Lectures on the Langlands program and conformal field theory". In: *Frontiers in Number Theory, Physics, and Geometry II*, pp. 387-533. Springer.

### Topological field theory
A symmetric monoidal functor $Z: \text{Bord}_n \to \mathcal{C}$ from the bordism category.

**Reference**: Atiyah, M. (1988). "Topological quantum field theories". *Institut des Hautes Études Scientifiques. Publications Mathématiques*, 68, 175-186.

### Extended TQFT
A functor from the $(\infty,n)$-category of bordisms to some target $(\infty,n)$-category.

**Reference**: Lurie, J. (2009). "On the classification of topological field theories". *Current Developments in Mathematics*, 2008, 129-280.

### Conformal field theory
A representation of the conformal algebra (Virasoro or current algebra) with specified properties.

**Reference**: Segal, G. (1988). "The definition of conformal field theory". In: *Topology, Geometry and Quantum Field Theory*, London Mathematical Society Lecture Note Series, vol. 308, pp. 421-577.

### Factorization algebra
A cosheaf-like structure $\mathcal{F}: \text{Open}(M) \to \mathcal{C}$ satisfying factorization axioms for disjoint unions.

**Reference**: Costello, K. & Gwilliam, O. (2017). *Factorization Algebras in Quantum Field Theory*, vol. 1. New Mathematical Monographs, vol. 31. Cambridge University Press.

### Chiral algebra
A vertex algebra or factorization algebra on a curve, central to 2d CFT.

**Reference**: Beilinson, A. & Drinfeld, V. (2004). *Chiral Algebras*. American Mathematical Society Colloquium Publications, vol. 51. American Mathematical Society.

### Vertex operator algebra
An algebra $V$ with a state-field correspondence $Y: V \to \text{End}(V)[[z,z^{-1}]]$ satisfying locality and other axioms.

**Reference**: Frenkel, I.B., Lepowsky, J., & Meurman, A. (1988). *Vertex Operator Algebras and the Monster*. Pure and Applied Mathematics, vol. 134. Academic Press.

### Deformation quantization
A formal deformation of the commutative algebra of functions to a noncommutative star product.

**Reference**: Kontsevich, M. (2003). "Deformation quantization of Poisson manifolds". *Letters in Mathematical Physics*, 66(3), 157-216.

### Drinfeld center
For a monoidal category $\mathcal{C}$, the center $Z(\mathcal{C})$ has objects $(A, \gamma)$ where $\gamma_X: A \otimes X \cong X \otimes A$ satisfies coherence.

**Reference**: Drinfeld, V.G. (1987). "Quantum groups". In: *Proceedings of the International Congress of Mathematicians*, vol. 1, pp. 798-820. American Mathematical Society.

### Hochschild cohomology
For an algebra $A$, the cohomology $HH^*(A) = \text{Ext}_{A^e}^*(A,A)$ where $A^e = A \otimes A^{op}$.

**Reference**: Hochschild, G. (1945). "On the cohomology groups of an associative algebra". *Annals of Mathematics*, 46(1), 58-67.

### Cyclic homology
The homology of the cyclic complex, related to Hochschild homology by the Connes' long exact sequence.

**Reference**: Connes, A. (1985). "Noncommutative differential geometry". *Institut des Hautes Études Scientifiques. Publications Mathématiques*, 62, 257-360.

### A∞-algebra
An algebra with operations $m_n: A^{\otimes n} \to A$ satisfying the $A_\infty$ relations:
$$\sum_{i+j+k=n} (-1)^{i+jk} m_{i+1+k}(\text{id}^{\otimes i} \otimes m_j \otimes \text{id}^{\otimes k}) = 0$$

**Reference**: Stasheff, J.D. (1963). "Homotopy associativity of H-spaces. I, II". *Transactions of the American Mathematical Society*, 108, 275-292, 293-312.

### A∞-category
A category enriched over chain complexes with higher composition operations satisfying $A_\infty$ coherence.

**Reference**: Fukaya, K. (1993). "Morse homotopy, $A_\infty$-category, and Floer homologies". In: *Proceedings of GARC Workshop on Geometry and Topology*, pp. 1-102.

### L∞-algebra
A graded vector space with brackets $\ell_n: \wedge^n L \to L$ satisfying generalized Jacobi identities.

**Reference**: Lada, T. & Stasheff, J. (1993). "Introduction to SH Lie algebras for physicists". *International Journal of Theoretical Physics*, 32(7), 1087-1103.

### dg-category
A category enriched over chain complexes with differential satisfying the Leibniz rule.

**Reference**: Bondal, A. & Kapranov, M. (1990). "Enhanced triangulated categories". *Mathematics of the USSR-Sbornik*, 70(1), 93-107.

### Spectral category
A category enriched over spectra, the stable version of simplicial categories.

**Reference**: Schwede, S. & Shipley, B. (2003). "Stable model categories are categories of modules". *Topology*, 42(1), 103-153.

### Shifted symplectic structure
A closed 2-form of degree $n$ on a derived stack inducing a non-degenerate pairing on the tangent complex.

**Reference**: Pantev, T., Toën, B., Vaquié, M., & Vezzosi, G. (2013). "Shifted symplectic structures". *Publications Mathématiques de l'IHÉS*, 117, 271-328.

### Factorization homology
For a factorization algebra $\mathcal{F}$ on $M$, the factorization homology $\int_M \mathcal{F}$ is the colimit over the Ran space.

**Reference**: Ayala, D. & Francis, J. (2015). "Factorization homology of topological manifolds". *Journal of Topology*, 8(4), 1045-1084.