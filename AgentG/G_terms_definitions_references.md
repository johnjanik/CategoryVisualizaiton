
---

### Classical Category Theory

*   **Abelian category**: An **additive category** `A` such that:
    1.  Every morphism has a **kernel** and a **cokernel**.
    2.  Every **monomorphism** is the kernel of its cokernel (it is a *normal monomorphism*).
    3.  Every **epimorphism** is the cokernel of its kernel (it is a *normal epimorphism*).
    The category of abelian groups, **Ab**, is the prototypical example.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter VIII, Section 1.

*   **Additive category**: A **preadditive category** that has a **zero object** and all finite **coproducts** (and thus all finite **products**, as they coincide in this context, called biproducts).
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter VIII, Section 1.

*   **Adjoint functor theorem**: A class of theorems providing sufficient conditions for a functor to have a left or right adjoint. The most common is the **General Adjoint Functor Theorem**: A functor `G: D -> C` has a left adjoint if and only if `D` is complete and `G` preserves all limits and satisfies the *solution set condition*: for each object `c` in `C`, there is a set of arrows `{f_i: c -> G(d_i)}` such that any arrow `h: c -> G(d)` factors as `h = G(k) ∘ f_i` for some `i` and some arrow `k: d_i -> d`.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter V, Section 6.

*   **Adjunction** (unit, counit; left and right adjoints): An adjunction between two categories `C` and `D` consists of a pair of functors `F: C -> D` (the **left adjoint**) and `G: D -> C` (the **right adjoint**), and a natural isomorphism `φ_{X,Y}: Hom_D(F(X), Y) ≅ Hom_C(X, G(Y))` for all objects `X` in `C` and `Y` in `D`. Equivalently, it is given by the functors `F`, `G` and two natural transformations: the **unit** `η: Id_C -> G ∘ F` and the **counit** `ε: F ∘ G -> Id_D`, which satisfy the **triangle identities**: `(εF) ∘ (Fη) = id_F` and `(Gε) ∘ (ηG) = id_G`.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter IV, Section 1.

*   **Automorphism**: An **isomorphism** from an object to itself. The set of all automorphisms of an object `X` forms a group under composition, denoted `Aut(X)`.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter I, Section 5.

*   **Balanced category**: A category in which every morphism that is both a **monomorphism** and an **epimorphism** is an **isomorphism**.
    *   **Reference:** Borceux, F. (1994). *Handbook of Categorical Algebra 1: Basic Category Theory*. Cambridge University Press. Definition 2.6.2.

*   **Category** (small, large, locally small): A category `C` consists of:
    1.  A collection of **objects**, `Ob(C)`.
    2.  A collection of **morphisms** (or arrows), `Mor(C)`.
    3.  Functions `dom, cod: Mor(C) -> Ob(C)` assigning a **domain** and **codomain** to each morphism.
    4.  For every object `X`, an **identity morphism** `id_X: X -> X`.
    5.  A **composition** operation: for any two morphisms `f: X -> Y` and `g: Y -> Z`, there is a morphism `g ∘ f: X -> Z`.
    This data must satisfy two axioms: **associativity** (`h ∘ (g ∘ f) = (h ∘ g) ∘ f`) and **identity** (`f ∘ id_X = f` and `id_Y ∘ f = f`).
    *   A category is **small** if `Ob(C)` and `Mor(C)` are sets.
    *   It is **large** if `Ob(C)` or `Mor(C)` are proper classes (e.g., **Set**, the category of all sets).
    *   It is **locally small** if for any two objects `X, Y`, the collection of morphisms `Hom_C(X, Y)` is a set.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter I, Sections 1-2.

*   **Category of elements**: For a presheaf `P: C^op -> Set`, its category of elements, denoted `∫ P`, is the category whose objects are pairs `(X, x)` where `X` is an object of `C` and `x ∈ P(X)`. A morphism from `(X, x)` to `(Y, y)` is a morphism `f: X -> Y` in `C` such that `P(f)(y) = x`. This construction is a key part of the Grothendieck construction.
    *   **Reference:** Mac Lane, S., & Moerdijk, I. (1992). *Sheaves in Geometry and Logic: A First Introduction to Topos Theory*. Springer. Chapter I, Section 5.

*   **Cauchy (Karoubi) completion**: The smallest category `Split(C)` containing a category `C` in which every idempotent `e: X -> X` (i.e., `e ∘ e = e`) splits. An idempotent splits if there exist morphisms `r: X -> Y` and `s: Y -> X` such that `e = s ∘ r` and `r ∘ s = id_Y`. The objects of `Split(C)` are pairs `(X, e)` where `e` is an idempotent on `X` in `C`.
    *   **Reference:** Borceux, F. (1994). *Handbook of Categorical Algebra 1: Basic Category Theory*. Cambridge University Press. Section 6.5.

*   **Comma category**: Given two functors `F: A -> C` and `G: B -> C`, the comma category `(F ↓ G)` has:
    *   **Objects**: Triples `(a, b, f)` where `a` is an object of `A`, `b` is an object of `B`, and `f: F(a) -> G(b)` is a morphism in `C`.
    *   **Morphisms**: A morphism from `(a, b, f)` to `(a', b', f')` is a pair of morphisms `(h: a -> a', k: b -> b')` such that the diagram `f' ∘ F(h) = G(k) ∘ f` commutes.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter II, Section 6.

*   **Composition** (associativity, identity laws): The operation `∘` that takes two morphisms `f: X -> Y` and `g: Y -> Z` and produces a morphism `g ∘ f: X -> Z`. It must satisfy:
    *   **Associativity**: `h ∘ (g ∘ f) = (h ∘ g) ∘ f` for any composable `f, g, h`.
    *   **Identity**: `f ∘ id_X = f` and `id_Y ∘ f = f` for `f: X -> Y`.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter I, Section 2.

*   **Contravariant functor**: A functor `F: C -> D` that reverses the direction of morphisms. Formally, it's a functor from the **opposite category** `C^op` to `D`. It maps an object `X` in `C` to `F(X)` in `D`, and a morphism `f: X -> Y` in `C` to a morphism `F(f): F(Y) -> F(X)` in `D`, such that `F(id_X) = id_{F(X)}` and `F(g ∘ f) = F(f) ∘ F(g)`.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter II, Section 1.

*   **Copower** (tensoring with a set or object): The copower of an object `X` in a category `C` with a set `S`, denoted `S · X`, is the coproduct of `S` copies of `X`, i.e., `∐_{s∈S} X`. More generally, in a category enriched over a monoidal category `V`, the tensoring of an object `X` in `C` with an object `v` in `V` is an object `v ⊗ X` in `C` representing the functor `Hom_C(v ⊗ X, -) ≅ Hom_V(v, Hom_C(X, -))`.
    *   **Reference:** Kelly, G. M. (1982). *Basic Concepts of Enriched Category Theory*. Cambridge University Press. Section 1.4.

*   **Copresheaf**: A functor `F: C -> Set`. This is simply another name for a **presheaf on the opposite category `C^op`**, or more commonly, just a covariant functor to **Set**.
    *   **Reference:** Riehl, E. (2017). *Category Theory in Context*. Dover Publications. Section 1.2.

*   **Coproduct**: The dual concept to a **product**. The coproduct of a family of objects `{X_i}_{i∈I}` is an object `∐_{i∈I} X_i` together with morphisms `ι_j: X_j -> ∐_{i∈I} X_i` (called injections) such that for any object `Y` and any family of morphisms `f_i: X_i -> Y`, there exists a unique morphism `f: ∐_{i∈I} X_i -> Y` such that `f ∘ ι_i = f_i` for all `i`.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter III, Section 3.

*   **Cosegment**: The dual of a segment object in a category. This concept is less common but appears in contexts like Reedy categories.
    *   **Reference:** Reedy, C. L. (1974). *Homotopy theory of model categories*. Unpublished manuscript, available online.

*   **Coslice category**: A special case of a **comma category**. For a fixed object `X` in a category `C`, the coslice category `(X ↓ C)` has:
    *   **Objects**: Pairs `(Y, f)` where `Y` is an object of `C` and `f: X -> Y` is a morphism.
    *   **Morphisms**: A morphism from `(Y, f)` to `(Z, g)` is a morphism `h: Y -> Z` in `C` such that `h ∘ f = g`.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter II, Section 6.

*   **Coequalizer**: The dual concept to an **equalizer**. For a pair of parallel morphisms `f, g: X -> Y`, their coequalizer is an object `Q` and a morphism `q: Y -> Q` such that `q ∘ f = q ∘ g`, and for any other object `Z` and morphism `h: Y -> Z` with `h ∘ f = h ∘ g`, there exists a unique morphism `u: Q -> Z` such that `h = u ∘ q`.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter III, Section 3.

*   **Coefficient** (in enriched/hyperdoctrine contexts): In enriched category theory, the "coefficients" for enrichment are the objects and morphisms of the monoidal category `V` over which the category is enriched. In Lawvere's hyperdoctrines, a "coefficient" object is an object in the base category whose fibers in the indexed category are used to form logical theories.
    *   **Reference:** Lawvere, F. W. (1969). *Adjointness in Foundations*. Dialectica, 23(3-4), 281-296.

*   **Coend**: The dual of an **end**. For a functor `F: C^op × C -> D`, its coend, denoted `∫^c F(c, c)`, is an object of `D` that is universal among objects `d` equipped with a **dinatural transformation** from `F` to the constant functor at `d`. Formally, it is a pair `(Q, ω)` where `Q` is an object of `D` and `ω: F ⇒ Δ_Q` is a dinatural transformation, such that for any other pair `(D, τ)`, there is a unique morphism `h: Q -> D` with `τ = Δ_h ∘ ω`.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter IX, Section 6.

*   **Coreflective subcategory**: A full subcategory `A` of `B` where the inclusion functor `I: A -> B` has a right adjoint `R: B -> A`, called the coreflector.
    *   **Reference:** Adámek, J., Herrlich, H., & Strecker, G. E. (2004). *Abstract and Concrete Categories: The Joy of Cats*. Dover Publications. Chapter III, Section 10.

*   **Covariant functor**: The default type of functor, often just called a **functor**. A functor `F: C -> D` is covariant if it preserves the direction of morphisms. It maps `f: X -> Y` to `F(f): F(X) -> F(Y)` and respects composition (`F(g ∘ f) = F(g) ∘ F(f)`) and identities (`F(id_X) = id_{F(X)}`).
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter I, Section 3.

*   **Dinatural transformation**: For a functor `F: C^op × C -> D`, a dinatural transformation `α` from `F` to an object `d` in `D` is a family of morphisms `α_X: F(X, X) -> d` for each `X` in `C`, such that for any morphism `f: X -> Y` in `C`, the following diagram commutes: `F(id_Y, f) ∘ α_Y = F(f, id_X) ∘ α_X`.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter IX, Section 4.

*   **Dual category** (opposite category): For a category `C`, its dual or opposite category `C^op` has the same objects as `C`, but for every morphism `f: X -> Y` in `C`, there is a corresponding morphism `f^op: Y -> X` in `C^op`. Composition is defined by `g^op ∘ f^op = (f ∘ g)^op`.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter II, Section 1.

*   **End**: For a functor `F: C^op × C -> D`, its end, denoted `∫_c F(c, c)`, is an object of `D` that is universal among objects `d` equipped with a **dinatural transformation** from the constant functor at `d` to `F`. Formally, it is a pair `(E, ω)` where `E` is an object of `D` and `ω: Δ_E ⇒ F` is a dinatural transformation, such that for any other pair `(D, τ)`, there is a unique morphism `h: D -> E` with `τ = ω ∘ Δ_h`. The set of natural transformations between two functors `F, G: C -> D` is the end `∫_c Hom_D(F(c), G(c))`.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter IX, Section 5.

*   **Equalizer**: For a pair of parallel morphisms `f, g: X -> Y`, their equalizer is an object `E` and a morphism `e: E -> X` such that `f ∘ e = g ∘ e`, and for any other object `Z` and morphism `m: Z -> X` with `f ∘ m = g ∘ m`, there exists a unique morphism `u: Z -> E` such that `m = e ∘ u`.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter III, Section 1.

*   **Essentially surjective functor**: A functor `F: C -> D` is essentially surjective if for every object `d` in `D`, there exists an object `c` in `C` and an isomorphism `F(c) ≅ d` in `D`.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter IV, Section 4.

*   **Exact category** (in the sense of Quillen): An **additive category** `E` equipped with a class of "admissible" short exact sequences `0 -> A -> B -> C -> 0` (where the first map is an "admissible monomorphism" and the second is an "admissible epimorphism") satisfying certain axioms. These axioms ensure that the class behaves like the class of all short exact sequences in an abelian category, making it a suitable setting for algebraic K-theory.
    *   **Reference:** Quillen, D. (1973). *Higher algebraic K-theory: I*. In *Algebraic K-theory, I: Higher K-theories* (pp. 85-147). Springer.

*   **Factorization system**: A pair of classes of morphisms `(E, M)` in a category `C` such that:
    1.  Both `E` and `M` are closed under composition and contain all isomorphisms.
    2.  Every morphism `f` in `C` can be factored as `f = m ∘ e` where `e ∈ E` and `m ∈ M`.
    3.  The factorization is unique up to a unique isomorphism: if `f = m' ∘ e'`, then there is a unique isomorphism `i` such that `e' = i ∘ e` and `m = m' ∘ i`. This is the orthogonality condition `E ⊥ M`.
    A common example is `(Epi, Mono)` for epimorphisms and monomorphisms in many categories like **Set**.
    *   **Reference:** Borceux, F. (1994). *Handbook of Categorical Algebra 1: Basic Category Theory*. Cambridge University Press. Section 4.4.

*   **Fully faithful functor**: A functor `F: C -> D` that is both **full** and **faithful**. This means the map `F: Hom_C(X, Y) -> Hom_D(F(X), F(Y))` is a bijection for all objects `X, Y` in `C`. A fully faithful functor induces an equivalence onto its image.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter I, Section 5.

*   **Functor** (covariant, contravariant): A structure-preserving map between categories. See **Covariant functor** and **Contravariant functor**.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter I, Section 3.

*   **Functor category**: For categories `C` and `D`, the functor category `D^C` (or `[C, D]`) has:
    *   **Objects**: Functors from `C` to `D`.
    *   **Morphisms**: Natural transformations between these functors.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter II, Section 1.

*   **Full functor**: A functor `F: C -> D` is full if for every pair of objects `X, Y` in `C`, the map on hom-sets `F: Hom_C(X, Y) -> Hom_D(F(X), F(Y))` is surjective.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter I, Section 5.

*   **Grothendieck fibration**: A functor `p: E -> B` is a fibration if for every object `e` in `E` and every morphism `f: b' -> p(e)` in `B`, there exists a **Cartesian morphism** `g: e' -> e` in `E` such that `p(g) = f`. A morphism `g` is Cartesian if for any `h` with `cod(h) = cod(g)` and `p(h) = p(g) ∘ k`, there is a unique `l` with `p(l) = k` such that `h = g ∘ l`.
    *   **Reference:** Grothendieck, A. (1971). *SGA 1: Revêtements étales et groupe fondamental*. Springer. Exposé VI.

*   **Grothendieck topology**: A structure on a category `C` that specifies for each object `U` a collection of "covering families" (sieves) `{U_i -> U}_{i∈I}`, subject to axioms analogous to those for open covers in topology. This allows one to define sheaves on `C` and forms the basis of site theory and topos theory.
    *   **Reference:** Mac Lane, S., & Moerdijk, I. (1992). *Sheaves in Geometry and Logic: A First Introduction to Topos Theory*. Springer. Chapter III, Section 2.

*   **Image** (regular image, categorical image):
    *   **Categorical Image**: The image of a morphism `f: X -> Y` is the smallest subobject of `Y` through which `f` factors. It can be constructed as the equalizer of the pair of morphisms `Y -> P` that are the cokernel of `f`.
    *   **Regular Image**: If `f` has a coequalizer `c` for its kernel pair, then the image is the equalizer of `c` and `c`. In a regular category, the image of `f: X -> Y` is constructed as the equalizer of the cokernel pair of `f`. In many concrete categories, this corresponds to the set-theoretic image.
    *   **Reference:** Borceux, F. (1994). *Handbook of Categorical Algebra 1: Basic Category Theory*. Cambridge University Press. Section 4.3.

*   **Initial object**: An object `0` in a category `C` such that for every object `X` in `C`, there exists a unique morphism `0 -> X`.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter III, Section 3.

*   **Isomorphism**: A morphism `f: X -> Y` for which there exists an inverse morphism `g: Y -> X` such that `g ∘ f = id_X` and `f ∘ g = id_Y`.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter I, Section 5.

*   **Kan extension** (left and right): Given functors `K: C -> D` and `F: C -> E`, a **left Kan extension** of `F` along `K`, denoted `Lan_K F`, is a functor `Lan_K F: D -> E` together with a natural transformation `η: F ⇒ (Lan_K F) ∘ K` that is universal. This means for any other functor `G: D -> E` and natural transformation `α: F ⇒ G ∘ K`, there is a unique natural transformation `δ: Lan_K F ⇒ G` such that `α = (δK) ∘ η`. The **right Kan extension** `Ran_K F` is defined dually.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter X, Section 1.

*   **Kernel**: For a morphism `f: X -> Y` in a category with a zero object, its kernel is the **equalizer** of `f` and the zero morphism `0: X -> Y`.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter VIII, Section 1.

*   **Lawvere theory**: A small category `T` with finite products, where every object is a finite power `X^n` of a distinguished object `X`. A model of the theory in a category `C` with finite products is a product-preserving functor `M: T -> C`. This provides a purely categorical way to define algebraic theories.
    *   **Reference:** Lawvere, F. W. (1963). *Functorial Semantics of Algebraic Theories*. PhD thesis, Columbia University. (Reprinted in *Reprints in Theory and Applications of Categories*, No. 5, 2004).

*   **Limit** (inverse limit, pullback, etc.): The limit of a diagram `F: J -> C` (where `J` is a small category) is an object `L` in `C` together with a family of morphisms `π_j: L -> F(j)` for each object `j` in `J` (forming a **cone**), such that for any other cone `(N, ψ_j)`, there is a unique morphism `u: N -> L` such that `ψ_j = π_j ∘ u` for all `j`.
    *   **Inverse limit**: A limit over a directed set `J^op`.
    *   **Pullback**: The limit of a diagram `X -> Z <- Y`.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter III, Section 1.

*   **Locally presentable category**: A category `C` that is **cocomplete** and has a set `S` of **presentable objects** such that every object in `C` is a filtered colimit of objects from `S`. An object `X` is `κ`-presentable if `Hom(X, -)` preserves `κ`-filtered colimits.
    *   **Reference:** Adámek, J., & Rosický, J. (1994). *Locally Presentable and Accessible Categories*. Cambridge University Press.

*   **Monomorphism**: A morphism `f: X -> Y` that is left-cancellable: for any two morphisms `g_1, g_2: Z -> X`, if `f ∘ g_1 = f ∘ g_2`, then `g_1 = g_2`. It is the categorical analogue of an injective function.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter I, Section 5.

*   **Multicategory**: A generalization of a category where a morphism can have a list of objects as its domain and a single object as its codomain. Composition is defined by substituting a morphism's output into one of the inputs of another. Also known as a colored operad.
    *   **Reference:** Leinster, T. (2004). *Higher Operads, Higher Categories*. Cambridge University Press. Chapter 2.

*   **Natural transformation** (vertical/horizontal composition): Given two parallel functors `F, G: C -> D`, a natural transformation `α: F ⇒ G` is a family of morphisms `α_X: F(X) -> G(X)` in `D`, one for each object `X` in `C`, such that for every morphism `f: X -> Y` in `C`, the **naturality square** commutes: `α_Y ∘ F(f) = G(f) ∘ α_X`.
    *   **Vertical composition**: If `β: G ⇒ H` is another natural transformation, their vertical composite `β ∘ α: F ⇒ H` is defined by `(β ∘ α)_X = β_X ∘ α_X`.
    *   **Horizontal composition**: Given `α: F ⇒ G: C -> D` and `β: F' ⇒ G': D -> E`, their horizontal composite `β ∗ α: F'F ⇒ G'G` is defined by `(β ∗ α)_X = β_{G(X)} ∘ F'(α_X) = G'(α_X) ∘ β_{F(X)}`.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter II, Sections 1 & 4.

*   **Natural isomorphism**: A **natural transformation** `α: F ⇒ G` where every component `α_X` is an **isomorphism**.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter II, Section 1.

*   **Nerve of a category**: A functor `N: Cat -> sSet` from the category of small categories to the category of simplicial sets. For a category `C`, `N(C)` is the simplicial set whose `n`-simplices are sequences of `n` composable morphisms in `C`: `X_0 -> X_1 -> ... -> X_n`.
    *   **Reference:** Goerss, P. G., & Jardine, J. F. (1999). *Simplicial Homotopy Theory*. Birkhäuser. Chapter I, Section 2.

*   **Opposite category**: See **Dual category**.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter II, Section 1.

*   **Power** (exponentials, internal homs): The power of an object `Y` by an object `X`, denoted `Y^X`, is an object that represents the functor `Hom(- × X, Y)`. This means there is a natural isomorphism `Hom(Z × X, Y) ≅ Hom(Z, Y^X)`. The object `Y^X` is also called the **exponential object** or **internal hom**, written `[X, Y]`. A category with all finite products and exponentials is a **Cartesian closed category**.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter IV, Section 6.

*   **Preadditive category**: A category enriched over the monoidal category of abelian groups (**Ab**). This means each hom-set `Hom(X, Y)` is an abelian group, and composition of morphisms is bilinear.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter VIII, Section 1.

*   **Product**: The limit of a diagram over a discrete category `J`. The product of a family of objects `{X_i}_{i∈I}` is an object `∏_{i∈I} X_i` together with morphisms `π_j: ∏_{i∈I} X_i -> X_j` (called projections) such that for any object `Y` and any family of morphisms `f_i: Y -> X_i`, there exists a unique morphism `f: Y -> ∏_{i∈I} X_i` such that `π_i ∘ f = f_i` for all `i`.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter III, Section 1.

*   **Pullback**: The limit of a cospan diagram `X -> Z <- Y`. It is an object `P` with morphisms `p_1: P -> X` and `p_2: P -> Y` such that `f ∘ p_1 = g ∘ p_2`, and this square is universal among all such squares.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter III, Section 1.

*   **Pushout**: The colimit of a span diagram `X <- Z -> Y`. It is the dual of a pullback.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter III, Section 3.

*   **Reflective subcategory**: A full subcategory `A` of `B` where the inclusion functor `I: A -> B` has a left adjoint `L: B -> A`, called the reflector.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter IV, Section 3.

*   **Representable functor**: A covariant functor `F: C -> Set` is representable if it is naturally isomorphic to a hom-functor `Hom_C(X, -)` for some object `X` in `C`. Dually, a contravariant functor `G: C^op -> Set` is representable if it is naturally isomorphic to `Hom_C(-, X)`. The object `X` is called the representing object.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter III, Section 2 (Yoneda Lemma).

*   **Retract** (section/retraction): A morphism `f: X -> Y` is a **retraction** if it has a right inverse, i.e., a morphism `s: Y -> X` (called a **section**) such that `f ∘ s = id_Y`. The object `Y` is then a retract of `X`.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter I, Section 5.

*   **Slice category**: A special case of a **comma category**. For a fixed object `X` in a category `C`, the slice category `(C ↓ X)` has:
    *   **Objects**: Pairs `(Y, f)` where `Y` is an object of `C` and `f: Y -> X` is a morphism.
    *   **Morphisms**: A morphism from `(Y, f)` to `(Z, g)` is a morphism `h: Y -> Z` in `C` such that `g ∘ h = f`.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter II, Section 6.

*   **Split exact sequence**: A short exact sequence `0 -> A -> B -> C -> 0` in an abelian category is split if it is equivalent to the sequence `0 -> A -> A ⊕ C -> C -> 0`. This is equivalent to the monomorphism `A -> B` having a retraction, or the epimorphism `B -> C` having a section.
    *   **Reference:** Weibel, C. A. (1994). *An Introduction to Homological Algebra*. Cambridge University Press. Section 1.3.

*   **Split monomorphism / split epimorphism**:
    *   A **split monomorphism** is a morphism `f: X -> Y` that has a left inverse (a retraction).
    *   A **split epimorphism** is a morphism `g: Y -> Z` that has a right inverse (a section).
    Every split mono is a monomorphism, and every split epi is an epimorphism.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter I, Section 5.

*   **Subobject** (subobject classifier in a topos):
    *   A **subobject** of an object `X` is an equivalence class of monomorphisms `m: S -> X`, where two monomorphisms `m_1: S_1 -> X` and `m_2: S_2 -> X` are equivalent if there is an isomorphism `i: S_1 -> S_2` such that `m_2 ∘ i = m_1`.
    *   A **subobject classifier** in a category with a terminal object `1` is an object `Ω` together with a monomorphism `true: 1 -> Ω` such that for any monomorphism `m: S -> X`, there is a unique morphism `χ_m: X -> Ω` (the characteristic function) for which the square with `m` and `true` is a pullback.
    *   **Reference:** Mac Lane, S., & Moerdijk, I. (1992). *Sheaves in Geometry and Logic: A First Introduction to Topos Theory*. Springer. Chapter IV, Section 1.

*   **Terminal object**: An object `1` in a category `C` such that for every object `X` in `C`, there exists a unique morphism `X -> 1`.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter III, Section 3.

*   **Universal arrow / universal property**: A universal property defines an object by its relationship to other objects via morphisms. A **universal arrow** from an object `X` to a functor `F: C -> D` is a pair `(c, u: X -> F(c))` where `c` is in `C`, such that for any other pair `(c', u': X -> F(c'))`, there is a unique morphism `h: c -> c'` in `C` with `u' = F(h) ∘ u`. Limits and adjoints are defined by universal properties.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter III, Section 1.

*   **Weak limit / weak colimit**: A cone (or cocone) that satisfies the existence part of the universal property for a limit (or colimit), but not necessarily the uniqueness part.
    *   **Reference:** Borceux, F. (1994). *Handbook of Categorical Algebra 1: Basic Category Theory*. Cambridge University Press. Definition 2.1.1 (Note).

*   **Zero object**: An object that is both **initial** and **terminal**.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter VIII, Section 1.

*   **Zero morphism**: In a category with a zero object `0`, the zero morphism between `X` and `Y` is the unique morphism `X -> 0 -> Y` that factors through the zero object. In a preadditive category, it is the additive identity element of the hom-group `Hom(X, Y)`.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter VIII, Section 1.

---

### Basic Higher Category Concepts

*   **∗Complicial set**: A variation of a simplicial set used in some models of (∞,n)-categories.
    *   **Reference:** Verity, D. (2008). *Complicial sets*. In *Fields Institute Communications* (Vol. 51, pp. 343-432). American Mathematical Society.

*   **Cellular set**: A presheaf on the category of "globes," similar to a globular set but with different face maps, used as a model for weak ω-categories.
    *   **Reference:** Berger, C. (2002). *A cellular nerve for higher categories*. Advances in Mathematics, 169(1), 118-175.

*   **Homotopy category**: For a category `C` with a notion of homotopy (e.g., a model category or any higher category), its homotopy category `Ho(C)` is the category with the same objects as `C`, but where morphisms are homotopy classes of morphisms in `C`. This collapses all higher-dimensional information into a 1-category.
    *   **Reference:** Quillen, D. (1967). *Homotopical Algebra*. Springer. Chapter I, Section 1.

*   **n-category**: A structure with objects (0-cells), morphisms (1-cells), 2-morphisms between morphisms, ..., up to n-morphisms between (n-1)-morphisms. Composition is defined at all levels.
    *   **Reference:** Leinster, T. (2004). *Higher Operads, Higher Categories*. Cambridge University Press. Chapter 1.

*   **∞-category**: A structure with k-morphisms for all `k ≥ 0`. It is a conceptual term with many formal models, such as **quasicategories**, **complete Segal spaces**, and **simplicial categories**. The most common usage refers to an **(∞,1)-category**, where all k-morphisms for `k > 1` are invertible (are equivalences).
    *   **Reference:** Lurie, J. (2009). *Higher Topos Theory*. Princeton University Press. Chapter 1.

*   **Weak n-category**: An n-category where the axioms of associativity and identity for composition hold only up to a higher, invertible morphism (an equivalence). These equivalences must themselves satisfy coherence laws.
    *   **Reference:** Baez, J. C., & Dolan, J. (1998). *Higher-dimensional algebra and topological quantum field theory*. Journal of Mathematical Physics, 36(11), 6073-6105. (arXiv:q-alg/9503002).

*   **Strict n-category**: An n-category where the axioms of associativity and identity for composition hold strictly (on the nose) at all levels.
    *   **Reference:** Leinster, T. (2004). *Higher Operads, Higher Categories*. Cambridge University Press. Chapter 1.

*   **Bicategory**: A weak 2-category. It has objects, 1-morphisms, and 2-morphisms. Composition of 1-morphisms is associative only up to a natural isomorphism (the associator), and identities hold up to natural isomorphisms (the unitors), which satisfy coherence axioms (the pentagon identity).
    *   **Reference:** Bénabou, J. (1967). *Introduction to Bicategories*. In *Reports of the Midwest Category Seminar* (pp. 1-77). Springer.

*   **Globular set**: A sequence of sets `G_0, G_1, G_2, ...` with pairs of source and target maps `s_n, t_n: G_{n+1} -> G_n` satisfying `s_n ∘ s_{n+1} = s_n ∘ t_{n+1}` and `t_n ∘ s_{n+1} = t_n ∘ t_{n+1}`. It is the basic "shape" for defining strict ∞-categories.
    *   **Reference:** Leinster, T. (2004). *Higher Operads, Higher Categories*. Cambridge University Press. Definition 1.2.1.

*   **Nerve of a category**: (See definition in Classical section). In higher category theory, this construction is fundamental for relating 1-categories to (∞,1)-categories, as the nerve of a 1-category is a quasicategory.
    *   **Reference:** Lurie, J. (2009). *Higher Topos Theory*. Princeton University Press. Proposition 1.1.2.7.

*   **Quasicategory**: A **simplicial set** `S` satisfying the *weak Kan condition* or *inner horn filling condition*: for any `0 < k < n`, any map from the inner horn `Λ^n_k -> S` can be extended to a map `Δ^n -> S`. This is the most widely used model for (∞,1)-categories.
    *   **Reference:** Lurie, J. (2009). *Higher Topos Theory*. Princeton University Press. Definition 1.1.1.1.

*   **Kan complex**: A **simplicial set** `K` where *every* horn `Λ^n_k -> K` (for `0 ≤ k ≤ n`) has a filler. This is a model for an **∞-groupoid** (an ∞-category where all morphisms are invertible).
    *   **Reference:** Lurie, J. (2009). *Higher Topos Theory*. Princeton University Press. Definition 1.2.5.1.

*   **Simplicial set**: A functor `X: Δ^op -> Set`, where `Δ` is the simplex category. It can be thought of as a collection of `n`-simplices for each `n ≥ 0`, with face and degeneracy maps specifying how they are glued together.
    *   **Reference:** Goerss, P. G., & Jardine, J. F. (1999). *Simplicial Homotopy Theory*. Birkhäuser. Chapter I, Definition 1.1.

*   **Complete Segal space**: A model for (∞,1)-categories. It is a simplicial space (a functor `Δ^op -> Top`) that is "fibrant" and satisfies the "Segal condition": the map `X_n -> X_1 ×_{X_0} ... ×_{X_0} X_1` is a weak homotopy equivalence. The completeness condition ensures it has equivalences.
    *   **Reference:** Rezk, C. (2001). *A model for the homotopy theory of homotopy theory*. Transactions of the American Mathematical Society, 353(3), 973-1007.

*   **Segal category**: A simplicial object in the category of categories that satisfies a condition analogous to that of a Segal space. It is another model for (∞,1)-categories.
    *   **Reference:** Hirschowitz, A., & Simpson, C. (2001). *Descente pour les n-champs*. arXiv:math/9807049.

*   **Homotopy hypothesis**: A conjecture (now largely considered a theorem in many contexts) stating that **n-groupoids** (weak n-categories where all morphisms are equivalences) are "the same as" **homotopy n-types**. For `n=∞`, it asserts an equivalence between the category of ∞-groupoids and the category of topological spaces (up to weak homotopy equivalence).
    *   **Reference:** Grothendieck, A. (1983). *Pursuing Stacks*. Manuscript. (A modern treatment is in Lurie, J. (2009). *Higher Topos Theory*. Princeton University Press. Section 1.2.5).

---

### Types of Higher Categories

*   **Cartesian closed category**: (See definition in Classical section). The concept extends to higher categories, e.g., a Cartesian closed (∞,1)-category is an (∞,1)-category with finite products and exponentials.
    *   **Reference:** Lurie, J. (2009). *Higher Topos Theory*. Princeton University Press. Section 2.4.1.

*   **Closed category**: (See definition in Classical section). A category with an internal hom-functor.
    *   **Reference:** Eilenberg, S., & Kelly, G. M. (1966). *Closed categories*. In *Proceedings of the Conference on Categorical Algebra* (pp. 421-562). Springer.

*   **Compact closed category**: A **symmetric monoidal category** in which every object `X` has a **dual** `X^*` (an object `X^*` with evaluation and coevaluation maps satisfying the zig-zag identities). This structure is key for representing traced categories and topological quantum field theories.
    *   **Reference:** Kelly, G. M., & Laplaza, M. L. (1980). *Coherence for compact closed categories*. Journal of Pure and Applied Algebra, 19, 193-213.

*   **Double category**: A structure with objects, horizontal morphisms, vertical morphisms, and 2-cells (squares) bounded by these morphisms. There are two independent composition laws (horizontal and vertical) that must satisfy an interchange law.
    *   **Reference:** Grandis, M., & Paré, R. (1999). *Limits in double categories*. Cahiers de Topologie et Géométrie Différentielle Catégoriques, 40(3), 162-220.

*   **Enriched category**: A category whose hom-objects are not sets, but objects in some **monoidal category** `V`. Composition and identities are defined using the monoidal structure of `V`.
    *   **Reference:** Kelly, G. M. (1982). *Basic Concepts of Enriched Category Theory*. Cambridge University Press.

*   **Internal category**: An object *inside* another category `C` that has the structure of a category. It consists of an "object of objects" `C_0` and an "object of morphisms" `C_1` in `C`, along with morphisms in `C` for source, target, identity, and composition that satisfy the category axioms expressed as commuting diagrams in `C`.
    *   **Reference:** Johnstone, P. T. (2002). *Sketches of an Elephant: A Topos Theory Compendium*. Oxford University Press. Volume 1, Section B2.1.

*   **Monoidal category**: A category `C` equipped with a bifunctor `⊗: C × C -> C` (the tensor product), a unit object `I`, and natural isomorphisms `α_{X,Y,Z}: (X ⊗ Y) ⊗ Z -> X ⊗ (Y ⊗ Z)` (the associator), `λ_X: I ⊗ X -> X` (left unitor), and `ρ_X: X ⊗ I -> X` (right unitor), satisfying the pentagon and triangle coherence axioms.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter VII, Section 1.

*   **Braided monoidal category**: A **monoidal category** equipped with a natural isomorphism `β_{X,Y}: X ⊗ Y -> Y ⊗ X` (the braiding) that satisfies the two hexagon axioms.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter XI, Section 1.

*   **Monoidal ∞-category**: An (∞,1)-category `C` equipped with a tensor product `⊗: C × C -> C` and a unit object `I`, where associativity and unit laws hold up to coherent homotopy. A common model is a simplicial set `C^⊗` over `Fin*` (the category of finite pointed sets) satisfying a Segal-like condition.
    *   **Reference:** Lurie, J. (2017). *Higher Algebra*. Available online from the author's website. Chapter 2.

*   **Omega-category (ω-category)**: Another name for a strict ∞-category.
    *   **Reference:** Street, R. (1987). *The algebra of oriented simplexes*. Journal of Pure and Applied Algebra, 49(3), 283-335.

*   **Pivotal category**: A **rigid monoidal category** (one where every object has a left and right dual) equipped with a natural isomorphism between the identity functor and the double dual functor (`X ≅ (X^*)^*`).
    *   **Reference:** Bakalov, B., & Kirillov, A. Jr. (2001). *Lectures on Tensor Categories and Modular Functors*. American Mathematical Society. Definition 2.4.1.

*   **Fusion category**: A semisimple rigid C*-tensor category with finitely many simple objects, one of which is the monoidal unit. These are fundamental in the study of conformal field theory and subfactors.
    *   **Reference:** Etingof, P., Gelaki, S., Nikshych, D., & Ostrik, V. (2015). *Tensor Categories*. American Mathematical Society. Definition 4.1.1.

*   **Modular tensor category**: A **braided fusion category** with an additional non-degeneracy condition on its braiding, captured by the "S-matrix". They are used to construct 3D topological quantum field theories.
    *   **Reference:** Turaev, V. G. (1994). *Quantum Invariants of Knots and 3-Manifolds*. De Gruyter. Chapter II.

*   **Symmetric monoidal category**: A **braided monoidal category** where the braiding `β` satisfies `β_{Y,X} ∘ β_{X,Y} = id_{X⊗Y}`.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter XI, Section 1.

*   **Virtual double category**: A generalization of a double category where vertical composition of 2-cells is not always defined, only for certain "composable pairs".
    *   **Reference:** Cruttwell, G. S. H., & Shulman, M. (2010). *A unified framework for generalized multicategories*. Theory and Applications of Categories, 24(21), 580-655.

---

### Morphisms & Cells

*   **k-morphism**: In a higher category, a `k`-morphism (or `k`-cell) is an element of the `k`-th level of the categorical structure. A 0-morphism is an object, a 1-morphism is an arrow between objects, a 2-morphism is an arrow between 1-morphisms, and generally, a `k`-morphism `α` has a `(k-1)`-morphism as its source and another as its target: `α: f -> g`, where `f, g` are `(k-1)`-morphisms.
    *   **Reference:** Leinster, T. (2004). *Higher Operads, Higher Categories*. Cambridge University Press. Chapter 1.

*   **2-morphism**: A morphism between 1-morphisms (arrows) in a 2-category or bicategory. Given two parallel 1-morphisms `f, g: X -> Y`, a 2-morphism `α: f ⇒ g` relates them.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter XII, Section 1.

*   **Higher morphism**: A generic term for a `k`-morphism where `k > 1`.
    *   **Reference:** Baez, J. C., & Shulman, M. (2010). *Lectures on n-Categories and Cohomology*. In *Towards Higher Categories* (pp. 1-68). Springer.

*   **Globular k-cell**: An element of the `k`-th set `C_k` in a **globular set**, which is the underlying combinatorial data for a strict ∞-category.
    *   **Reference:** Leinster, T. (2004). *Higher Operads, Higher Categories*. Cambridge University Press. Definition 1.2.1.

*   **Icon**: In 2-category theory, given two pseudofunctors `F, G: A -> B` between bicategories, an icon `α: F ⇒ G` is a family of 1-morphisms `α_X: F(X) -> G(X)` for each object `X` in `A`, together with a 2-isomorphism `α_f: G(f) ∘ α_X ⇒ α_Y ∘ F(f)` for each 1-morphism `f: X -> Y` in `A`, satisfying a coherence condition for composition. It is a "laxer" notion than a pseudonatural transformation.
    *   **Reference:** Lack, S. (2010). *A 2-categories companion*. In *Towards Higher Categories* (pp. 105-191). Springer. Section 3.

*   **Lax natural transformation**: Between two functors `F, G: B -> C` of bicategories, a lax natural transformation `α` consists of:
    1.  A 1-morphism `α_X: F(X) -> G(X)` for each object `X` in `B`.
    2.  A 2-morphism `α_f: G(f) ∘ α_X ⇒ α_Y ∘ F(f)` for each 1-morphism `f: X -> Y` in `B`.
    These must satisfy coherence axioms relating to composition and identities of 1-morphisms in `B`.
    *   **Reference:** Borceux, F. (1994). *Handbook of Categorical Algebra 2: Categories and Structures*. Cambridge University Press. Definition 7.5.1.

*   **Oplax natural transformation**: The dual of a lax natural transformation, where the 2-morphism has the opposite direction: `α_f: α_Y ∘ F(f) ⇒ G(f) ∘ α_X`.
    *   **Reference:** Borceux, F. (1994). *Handbook of Categorical Algebra 2: Categories and Structures*. Cambridge University Press. Definition 7.5.1.

*   **Pseudonatural transformation**: A **lax natural transformation** where the structure 2-morphisms `α_f` are all invertible (isomorphisms). This is the standard notion of "natural transformation" between functors of bicategories.
    *   **Reference:** Leinster, T. (2004). *Higher Operads, Higher Categories*. Cambridge University Press. Section 1.4.

*   **Modification**: A transformation between **pseudonatural transformations**. Given two pseudonatural transformations `α, β: F ⇒ G` between functors of bicategories, a modification `m: α ⇒ β` is a family of 2-morphisms `m_X: α_X ⇒ β_X` for each object `X`, satisfying a coherence condition that makes them "natural" with respect to the 1-morphisms of the source bicategory. Modifications are the 3-morphisms in the 3-category of bicategories.
    *   **Reference:** Bénabou, J. (1967). *Introduction to Bicategories*. In *Reports of the Midwest Category Seminar* (pp. 1-77). Springer.

*   **Equivalence in higher categories**: An ∞-functor `F: C -> D` is an equivalence if it is:
    1.  **Essentially surjective on objects**: For every object `d` in `D`, there is an object `c` in `C` and an equivalence `F(c) ≃ d`.
    2.  **Fully faithful**: For every pair of objects `c_1, c_2` in `C`, the induced map on mapping spaces `Map_C(c_1, c_2) -> Map_D(F(c_1), F(c_2))` is a weak homotopy equivalence.
    Equivalently, `F` is an equivalence if there exists a functor `G: D -> C` and natural equivalences `G ∘ F ≃ Id_C` and `F ∘ G ≃ Id_D`.
    *   **Reference:** Lurie, J. (2009). *Higher Topos Theory*. Princeton University Press. Definition 1.2.7.2.

*   **Adjoint equivalence**: An **adjunction** `F ⊣ G` where the unit `η: Id -> G ∘ F` and counit `ε: F ∘ G -> Id` are both natural isomorphisms (or equivalences in a higher-categorical context). An adjoint equivalence is a specific type of **equivalence of categories**.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter IV, Section 4. For the higher-categorical version, see Lurie, J. (2009). *Higher Topos Theory*. Princeton University Press. Proposition 5.2.4.6.

---

### Functors & Transformations

*   **∞-functor**: A morphism between ∞-categories. In the model of **quasicategories**, an ∞-functor `F: C -> D` is simply a map of simplicial sets.
    *   **Reference:** Lurie, J. (2009). *Higher Topos Theory*. Princeton University Press. Definition 1.2.1.1.

*   **Functor between bicategories**: A structure-preserving map between bicategories. There are several notions:
    *   **Strict functor**: Preserves composition and identities on the nose.
    *   **Pseudofunctor** (or homomorphism of bicategories): Preserves composition and identities up to coherent 2-isomorphisms. This is the most common notion.
    *   **Lax functor**: Preserves composition and identities up to a non-invertible 2-morphism transformation.
    *   **Reference:** Bénabou, J. (1967). *Introduction to Bicategories*. In *Reports of the Midwest Category Seminar* (pp. 1-77). Springer.

*   **Homotopy coherent diagram**: A diagram of objects and morphisms in a higher category where the commutativity conditions are relaxed to hold only up to specified, coherent higher morphisms (homotopies). For example, a triangle `h ∘ f = g` might be replaced by a 2-morphism `α: h ∘ f ⇒ g`.
    *   **Reference:** Cordier, J. M., & Porter, T. (1989). *Homotopy coherent category theory*. Transactions of the American Mathematical Society, 313(1), 1-41.

*   **Lax functor**: A map `F: B -> C` between bicategories that sends objects to objects, 1-morphisms to 1-morphisms, and 2-morphisms to 2-morphisms, equipped with comparison 2-morphisms `F_{f,g}: F(f) ∘ F(g) ⇒ F(f ∘ g)` and `F_X: I_{F(X)} ⇒ F(I_X)` that satisfy coherence axioms.
    *   **Reference:** Gray, J. W. (1974). *Formal Category Theory: Adjointness for 2-Categories*. Springer.

*   **Oplax functor**: The dual of a lax functor, with comparison maps `F(f ∘ g) ⇒ F(f) ∘ F(g)` and `F(I_X) ⇒ I_{F(X)}`.
    *   **Reference:** Street, R. (1972). *The formal theory of monads*. Journal of Pure and Applied Algebra, 2(2), 149-168.

*   **Pseudofunctor**: A **lax functor** where the comparison 2-morphisms are all invertible (isomorphisms).
    *   **Reference:** Bénabou, J. (1967). *Introduction to Bicategories*. In *Reports of the Midwest Category Seminar* (pp. 1-77). Springer.

*   **Transformation between ∞-functors**: In the quasicategory model, a natural transformation between two ∞-functors `F, G: C -> D` is a map of simplicial sets `α: C × Δ^1 -> D` whose restriction to `C × {0}` is `F` and to `C × {1}` is `G`.
    *   **Reference:** Lurie, J. (2009). *Higher Topos Theory*. Princeton University Press. Definition 1.2.2.1.

*   **Natural isomorphism up to higher equivalence**: Two natural transformations `α, β` between ∞-functors are considered equivalent if there is a "homotopy" between them. In the quasicategory model, this means they lie in the same connected component of the mapping space `Map_{D^C}(F, G)`.
    *   **Reference:** Lurie, J. (2009). *Higher Topos Theory*. Princeton University Press. Section 1.2.2.

---

### Limits & Colimits

*   **Homotopy colimit (hocolim)**: The left derived functor of the colimit functor. In a model category, it is computed by taking a cofibrant replacement of the diagram before taking the ordinary colimit. It is the "correct" notion of colimit in a homotopical setting.
    *   **Reference:** Hovey, M. (1999). *Model Categories*. American Mathematical Society. Chapter 5.

*   **Homotopy limit (holim)**: The right derived functor of the limit functor. In a model category, it is computed by taking a fibrant replacement of the diagram before taking the ordinary limit.
    *   **Reference:** Hovey, M. (1999). *Model Categories*. American Mathematical Society. Chapter 5.

*   **∞-categorical colimit**: The colimit in an (∞,1)-category. For a diagram `F: J -> C`, its colimit is an object `colim F` representing the functor `Map_C(colim F, -) ≃ lim Map_C(F(-), -)`. In the quasicategory model, it is a cocone that is a terminal object in the ∞-category of cocones.
    *   **Reference:** Lurie, J. (2009). *Higher Topos Theory*. Princeton University Press. Section 1.2.13.

*   **∞-categorical limit**: The limit in an (∞,1)-category. For a diagram `F: J -> C`, its limit is an object `lim F` representing the functor `Map_C(-, lim F) ≃ lim Map_C(-, F(-))`. In the quasicategory model, it is a cone that is a terminal object in the ∞-category of cones.
    *   **Reference:** Lurie, J. (2009). *Higher Topos Theory*. Princeton University Press. Section 1.2.13.

*   **Weighted limit**: A generalization of limits. Given a diagram `F: D -> C` and a "weight" functor `W: D -> Set`, the `W`-weighted limit of `F` is an object `lim_W F` in `C` that represents the functor `Hom_C(-, lim_W F) ≅ Nat(W, Hom_C(-, F))`.
    *   **Reference:** Kelly, G. M. (1982). *Basic Concepts of Enriched Category Theory*. Cambridge University Press. Chapter 3.

*   **Bicolimit**: The notion of colimit in a bicategory, which is defined up to equivalence rather than unique isomorphism.
    *   **Reference:** Street, R. (1980). *Fibrations in bicategories*. Cahiers de Topologie et Géométrie Différentielle Catégoriques, 21(2), 111-160.

*   **Flexible limit**: A type of 2-categorical limit that is better behaved than stricter notions.
    *   **Reference:** Bird, G. J., Kelly, G. M., Power, A. J., & Street, R. H. (1993). *Flexible limits for 2-categories*. Journal of Pure and Applied Algebra, 89(3), 215-239.

*   **Kan extension in higher categories**: A generalization of the classical **Kan extension** to higher categories. Given ∞-functors `K: C -> D` and `F: C -> E`, the left Kan extension `Lan_K F` is the ∞-functor `D -> E` that is left adjoint to the restriction functor `K^*: E^D -> E^C`. It can be computed by a colimit formula.
    *   **Reference:** Lurie, J. (2009). *Higher Topos Theory*. Princeton University Press. Chapter 4.

*   **Lax limit**: A weak notion of limit in a 2-category where the universal cone is not required to commute, but is equipped with comparison 2-cells satisfying coherence conditions.
    *   **Reference:** Street, R. (1974). *Limits and colimits in a 2-category*. Cahiers de Topologie et Géométrie Différentielle Catégoriques, 15(3), 267-293.

*   **Pseudolimit**: The standard notion of limit in a 2-category, where the universal cone commutes up to coherent isomorphisms.
    *   **Reference:** Kelly, G. M. (1989). *Elementary observations on 2-categorical limits*. Bulletin of the Australian Mathematical Society, 39(2), 301-317.

*   **End** (as a limiting construction): (See definition in Classical section). The end `∫_c F(c, c)` can be constructed as the equalizer of two maps between products, making it a specific type of limit. This construction generalizes to higher categories.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter IX, Section 5. For the higher version, see Lurie, J. (2017). *Higher Algebra*. Section 4.2.3.

*   **Bilimit**: A limit construction in a double category that takes both the horizontal and vertical structures into account simultaneously.
    *   **Reference:** Grandis, M., & Paré, R. (1999). *Limits in double categories*. Cahiers de Topologie et Géométrie Différentielle Catégoriques, 40(3), 162-220.

---

### Adjunctions & Duality

*   **Adjunction in bicategories**: An adjunction between bicategories `C` and `D` consists of pseudofunctors `F: C -> D` and `G: D -> C`, and pseudonatural transformations `η: Id_C ⇒ G ∘ F` and `ε: F ∘ G ⇒ Id_D` satisfying the triangle identities up to invertible modifications.
    *   **Reference:** Gray, J. W. (1974). *Formal Category Theory: Adjointness for 2-Categories*. Springer.

*   **Biadjunction**: Another term for an **adjunction in bicategories**.
    *   **Reference:** Leinster, T. (2004). *Higher Operads, Higher Categories*. Cambridge University Press. Section 1.5.

*   **Lax adjunction**: An adjunction between bicategories where the functors `F, G` are lax functors and the unit/counit are lax natural transformations, satisfying the triangle identities in a lax sense.
    *   **Reference:** Gray, J. W. (1974). *Formal Category Theory: Adjointness for 2-Categories*. Springer.

*   **∞-adjunction**: An adjunction between ∞-categories. It consists of two ∞-functors `F: C -> D` and `G: D -> C` and a natural equivalence `Map_D(F(c), d) ≃ Map_C(c, G(d))`.
    *   **Reference:** Lurie, J. (2009). *Higher Topos Theory*. Princeton University Press. Chapter 5.

*   **Coend calculus**: The collection of formal properties and computational rules for working with **ends** and **coends**, such as the Fubini theorem for ends/coends and the ninja-yoneda lemma.
    *   **Reference:** Riehl, E. (2017). *Category Theory in Context*. Dover Publications. Chapter 6.

*   **Dualizable object**: In a monoidal category, an object `X` is dualizable if it has a dual `X^*` equipped with evaluation `ev: X^* ⊗ X -> I` and coevaluation `coev: I -> X ⊗ X^*` maps satisfying the zig-zag identities.
    *   **Reference:** Etingof, P., Gelaki, S., Nikshych, D., & Ostrik, V. (2015). *Tensor Categories*. American Mathematical Society. Section 2.10.

*   **Fully dualizable object**: A concept in a symmetric monoidal (∞,n)-category. An object is fully dualizable if it has a dual not just with respect to the 1-category structure, but in a way that is compatible with all higher dimensions. This is a key ingredient in the Cobordism Hypothesis.
    *   **Reference:** Lurie, J. (2009). *On the classification of topological field theories*. In *Current Developments in Mathematics, 2008* (pp. 129-280). International Press.

*   **Serre duality**: A duality theorem in algebraic geometry. For a smooth projective variety `X` of dimension `n` over a field `k`, there is a natural isomorphism `H^i(X, F)^* ≅ H^{n-i}(X, F^∨ ⊗ ω_X)`, where `F` is a coherent sheaf, `F^∨` is its dual, and `ω_X` is the canonical sheaf. This has been vastly generalized in derived algebraic geometry.
    *   **Reference:** Hartshorne, R. (1977). *Algebraic Geometry*. Springer. Chapter III, Section 7.

*   **Verdier duality**: A generalization of Poincaré duality to sheaves. For a locally compact Hausdorff space `X` and a sheaf of abelian groups `F` on `X`, there is a duality `RHom(F, f^! k) ≅ RΓ_c(X, F)^*`, where `f^!` is the exceptional inverse image functor for the map `f: X -> pt`.
    *   **Reference:** Kashiwara, M., & Schapira, P. (1990). *Sheaves on Manifolds*. Springer. Chapter 3.

*   **Grothendieck duality**: A framework of duality theorems in algebraic geometry, generalizing both Serre and Verdier duality to morphisms `f: X -> Y` of schemes. It involves a "dualizing complex" `Rf^! O_Y` on `X` and establishes an adjunction between the derived pushforward `Rf_*` and a right adjoint `Rf^!`, the "exceptional inverse image functor".
    *   **Reference:** Hartshorne, R. (1966). *Residues and Duality*. Springer.

---

### Monads & Algebras

*   **Monad in a bicategory**: A monad on an object `X` in a bicategory `B` is a 1-morphism `T: X -> X`, together with 2-morphisms `μ: T ∘ T ⇒ T` (multiplication) and `η: Id_X ⇒ T` (unit) satisfying the monad axioms (associativity and unit laws).
    *   **Reference:** Street, R. (1972). *The formal theory of monads*. Journal of Pure and Applied Algebra, 2(2), 149-168.

*   **Comonad**: The dual of a monad. It consists of an endofunctor `T` with natural transformations `δ: T -> T^2` (comultiplication) and `ε: T -> Id` (counit) satisfying dual axioms.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter VI, Section 1.

*   **Eilenberg–Moore object**: For a monad `(T, μ, η)` in a bicategory `B` on an object `X`, its Eilenberg-Moore object is an object `X^T` and a 1-morphism `U: X^T -> X` equipped with an action `a: T ∘ U ⇒ U` which is universal among all such objects with an action. It is the object of "algebras".
    *   **Reference:** Street, R. (1972). *The formal theory of monads*. Journal of Pure and Applied Algebra, 2(2), 149-168.

*   **Kleisli object**: For a monad `(T, μ, η)` in a bicategory `B` on an object `X`, its Kleisli object is an object `X_T` and a 1-morphism `F: X -> X_T` which is universal among maps from `X` to objects `Y` equipped with a "monad-to-morphism" transformer. It is the object of "free algebras".
    *   **Reference:** Street, R. (1972). *The formal theory of monads*. Journal of Pure and Applied Algebra, 2(2), 149-168.

*   **Distributive law**: A natural transformation `λ: ST -> TS` for two monads `S` and `T` on the same category, satisfying coherence conditions that allow the monads to be composed into a single monad on `TS`.
    *   **Reference:** Beck, J. (1969). *Distributive laws*. In *Seminar on Triples and Categorical Homology Theory* (pp. 119-140). Springer.

*   **Algebras for a monad**: For a monad `(T, μ, η)` on a category `C`, a `T`-algebra is a pair `(X, h)` where `X` is an object of `C` and `h: T(X) -> X` is a morphism such that `h ∘ T(h) = h ∘ μ_X` and `h ∘ η_X = id_X`.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter VI, Section 2.

*   **Coalgebras**: The dual concept. For a comonad `(T, δ, ε)`, a `T`-coalgebra is a pair `(X, k)` where `k: X -> T(X)` satisfies dual axioms.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter VI, Section 2.

*   **Monadic functor**: A functor `U: D -> C` that "creates" a monad `T = U ∘ F` (where `F` is its left adjoint) in such a way that `D` is equivalent to the category of `T`-algebras.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter VI, Section 3.

*   **Barr–Beck theorem**: Gives necessary and sufficient conditions for a functor `U: D -> C` with a left adjoint to be **monadic**. The key condition is that `U` reflects isomorphisms and creates coequalizers of `U`-split pairs.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter VI, Section 7.

*   **Lax algebra**: For a monad `T` in a 2-category, a lax `T`-algebra on an object `X` is a morphism `a: T(X) -> X` together with 2-cells `a ∘ T(a) ⇒ a ∘ μ_X` and `id_X ⇒ a ∘ η_X` satisfying coherence conditions.
    *   **Reference:** Street, R. (1972). *The formal theory of monads*. Journal of Pure and Applied Algebra, 2(2), 149-168.

*   **Pseudo-monad**: A monad in the bicategory **Cat**, i.e., an endofunctor `T` on a category `C` where the multiplication and unit are natural isomorphisms satisfying coherence axioms only up to further isomorphisms. More generally, a monad in any bicategory.
    *   **Reference:** Marmolejo, F. (1999). *Distributive laws for pseudomonads*. Theory and Applications of Categories, 5(5), 91-147.

*   **Pseudo-algebra**: An algebra for a **pseudo-monad**, where the algebra structure maps are themselves isomorphisms satisfying coherence conditions.
    *   **Reference:** Marmolejo, F. (1999). *Distributive laws for pseudomonads*. Theory and Applications of Categories, 5(5), 91-147.

---

### Operads & Algebraic Structures

*   **Operad**: A mathematical structure that encodes operations with multiple inputs and one output. A symmetric operad `P` in a symmetric monoidal category `C` consists of an object `P(n)` of "n-ary operations" for each `n ≥ 0`, equipped with composition maps and an action of the symmetric group `S_n` on `P(n)`, satisfying coherence axioms.
    *   **Reference:** May, J. P. (1972). *The Geometry of Iterated Loop Spaces*. Springer.

*   **Multicategory**: A generalization of a category where a morphism can have a sequence of objects as its domain. It is equivalent to the notion of a **colored operad**.
    *   **Reference:** Leinster, T. (2004). *Higher Operads, Higher Categories*. Cambridge University Press. Chapter 2.

*   **PROP**: A structure similar to an operad, but encoding operations with multiple inputs and multiple outputs. It stands for "PROducts and Permutations".
    *   **Reference:** Mac Lane, S. (1965). *Categorical algebra*. Bulletin of the American Mathematical Society, 71(1), 40-106.

*   **Lawvere theory**: (See definition in Classical section). A categorical way to encode an algebraic theory. It is equivalent to a specific type of operad.
    *   **Reference:** Lawvere, F. W. (1963). *Functorial Semantics of Algebraic Theories*. PhD thesis, Columbia University.

*   **Topological operad**: An operad enriched in the category of topological spaces.
    *   **Reference:** May, J. P. (1972). *The Geometry of Iterated Loop Spaces*. Springer.

*   **Symmetric operad**: The standard notion of an operad, with actions of the symmetric groups.
    *   **Reference:** Loday, J. L., & Vallette, B. (2012). *Algebraic Operads*. Springer.

*   **Cyclic operad**: A symmetric operad with additional structure that allows inputs to be cyclically permuted with the output, relevant for cyclic homology.
    *   **Reference:** Getzler, E., & Kapranov, M. M. (1995). *Cyclic operads and cyclic homology*. In *Geometry, Topology, & Physics* (pp. 167-201). International Press.

*   **Modular operad**: A generalization of a cyclic operad that allows for "graph-like" compositions, relevant to the moduli space of curves and quantum field theory.
    *   **Reference:** Getzler, E., & Kapranov, M. M. (1998). *Modular operads*. Compositio Mathematica, 110(1), 65-126.

*   **Algebra over an operad**: An object `X` in a category `C` equipped with morphisms `P(n) ⊗ X^n -> X` that are compatible with the operad's composition structure. This formalizes the notion of an object having the algebraic structure encoded by `P`.
    *   **Reference:** May, J. P. (1972). *The Geometry of Iterated Loop Spaces*. Springer.

*   **Coalgebra over an operad**: The dual notion, with maps `X -> P(n) ⊗ X^n`.
    *   **Reference:** Fresse, B. (2017). *Homotopy of Operads and Grothendieck-Teichmüller Groups*. American Mathematical Society.

*   **∞-operad**: A homotopy-coherent version of an operad. In the language of ∞-categories, it is an ∞-functor from a category of trees `Ω` to an ∞-category `C` that satisfies a Segal-like condition.
    *   **Reference:** Lurie, J. (2017). *Higher Algebra*. Available online from the author's website. Chapter 2.

*   **Dendroidal set**: A presheaf on the category of trees `Ω`, used as a model for ∞-operads in the same way simplicial sets are used for ∞-categories.
    *   **Reference:** Moerdijk, I., & Weiss, I. (2007). *Dendroidal sets*. Algebraic & Geometric Topology, 7(3), 1441-1470.

*   **Colored operad**: An operad where operations have specified "types" or "colors" for their inputs and outputs. This is equivalent to a **multicategory**.
    *   **Reference:** Leinster, T. (2004). *Higher Operads, Higher Categories*. Cambridge University Press. Chapter 2.

*   **Properad**: A structure between an operad and a PROP, allowing for operations with multiple inputs and multiple outputs, but with a more restricted "connected graph" composition structure than PROPs.
    *   **Reference:** Vallette, B. (2007). *A Koszul duality for PROPs*. Transactions of the American Mathematical Society, 359(10), 4865-4943.

*   **∞-properad**: A homotopy-coherent version of a properad.
    *   **Reference:** Haugseng, R. (2014). *The higher structure of factorization homology*. arXiv:1409.0817.
---

### Topology & Homotopy Theory

*   **Classifying space**: For a topological group `G`, its classifying space `BG` is the base space of a universal principal `G`-bundle `EG -> BG`. `BG` is unique up to homotopy equivalence and has the property that homotopy classes of maps `[X, BG]` are in natural bijection with isomorphism classes of principal `G`-bundles over `X`. More generally, for a category `C`, its classifying space is the geometric realization of its **nerve**, `B(C) = |N(C)|`.
    *   **Reference:** Hatcher, A. (2002). *Algebraic Topology*. Cambridge University Press. Section 1.B (for groups); Segal, G. (1968). *Classifying spaces and spectral sequences*. Publications Mathématiques de l'IHÉS, 34, 105-112 (for categories).

*   **Delooping**: The process of constructing a space `Y` from a space `X` such that `X` is homotopy equivalent to the loop space of `Y`, i.e., `X ≃ ΩY`. A space `X` that admits a delooping is called a grouplike space. The delooping principle states that a grouplike `A_n`-space can be delooped `n` times.
    *   **Reference:** May, J. P. (1972). *The Geometry of Iterated Loop Spaces*. Springer. Chapter 7.

*   **Loop space**: For a pointed topological space `(X, x_0)`, its loop space `ΩX` is the space of all continuous maps from the circle `S^1` to `X` that send the basepoint of `S^1` to `x_0`, equipped with the compact-open topology. The loop space functor `Ω` is right adjoint to the suspension functor `Σ`.
    *   **Reference:** Hatcher, A. (2002). *Algebraic Topology*. Cambridge University Press. Section 4.A.

*   **Loop space object**: The internal version of a loop space in a category with finite limits. For a pointed object `(X, x_0: * -> X)`, its loop space object `ΩX` is the pullback of the diagram `* -> X <- *`, where the maps are given by `x_0`. In an (∞,1)-topos, this is the homotopy pullback `* ×_X *`.
    *   **Reference:** Lurie, J. (2009). *Higher Topos Theory*. Princeton University Press. Section 1.1.3.

*   **Mapping space**: In topology, for spaces `X` and `Y`, the mapping space `Map(X, Y)` is the set of continuous functions from `X` to `Y`, equipped with a topology (usually the compact-open topology). In higher category theory, the mapping space `Map_C(X, Y)` between two objects `X, Y` in an ∞-category `C` is an ∞-groupoid (often modeled as a Kan complex) whose 0-cells are the morphisms `X -> Y`, 1-cells are homotopies between them, and so on.
    *   **Reference:** May, J. P. (1999). *A Concise Course in Algebraic Topology*. University of Chicago Press. Chapter 5 (for topology); Lurie, J. (2009). *Higher Topos Theory*. Princeton University Press. Section 1.2.2 (for ∞-categories).

*   **Fundamental ∞-groupoid**: For a topological space `X`, its fundamental ∞-groupoid `Π_∞(X)` is an ∞-groupoid that captures the full homotopy type of `X`. Its objects are the points of `X`, morphisms are paths, 2-morphisms are homotopies between paths, etc. It is modeled by the Kan complex `Sing(X)` (the singular simplicial set of `X`).
    *   **Reference:** Lurie, J. (2009). *Higher Topos Theory*. Princeton University Press. Section 1.2.5.

*   **Homotopy fiber**: For a map `f: X -> Y` of spaces, the homotopy fiber over a point `y ∈ Y` is the space `hofib(f)_y` defined by the homotopy pullback square of `* -> Y <- X`. Concretely, it can be modeled as the space of pairs `(x, p)` where `x ∈ X` and `p` is a path from `f(x)` to `y` in `Y`.
    *   **Reference:** May, J. P. (1999). *A Concise Course in Algebraic Topology*. University of Chicago Press. Chapter 7.

*   **Homotopy n-type**: A topological space `X` is a homotopy `n`-type (or `n`-type) if its homotopy groups `π_k(X, x)` are trivial for all `k > n` and all basepoints `x`. Any space `X` has an associated `n`-type, its `n`-th Postnikov section `P_n(X)`.
    *   **Reference:** Hatcher, A. (2002). *Algebraic Topology*. Cambridge University Press. Section 4.3.

*   **Homotopy quotient**: For a group `G` acting on a space `X`, the homotopy quotient is the space `X_{hG} = (EG × X)/G`, where `EG` is the universal `G`-space. It is a homotopy-invariant version of the ordinary orbit space `X/G` and is the colimit of the action groupoid diagram in the ∞-category of spaces.
    *   **Reference:** May, J. P. (1999). *A Concise Course in Algebraic Topology*. University of Chicago Press. Chapter 17.

*   **Stabilization**: A general process that turns a sequence of objects or categories into a "stable" one, where the suspension functor is an equivalence. For example, the stable homotopy category of spectra is obtained from the category of pointed spaces by formally inverting the suspension functor.
    *   **Reference:** Adams, J. F. (1974). *Stable Homotopy and Generalised Homology*. University of Chicago Press.

*   **Suspension**: For a pointed topological space `(X, x_0)`, its reduced suspension `ΣX` is the quotient space `(X × I) / (X × \{0\} ∪ X × \{1\} ∪ \{x_0\} × I)`. The suspension functor `Σ` is left adjoint to the loop space functor `Ω`.
    *   **Reference:** Hatcher, A. (2002). *Algebraic Topology*. Cambridge University Press. Chapter 0.

---

### Model Structures

*   **Model category**: A category `C` that is complete and cocomplete, equipped with three classes of morphisms (weak equivalences `W`, fibrations `F`, cofibrations `Cof`) satisfying five axioms (2-out-of-3, retracts, lifting, and factorization). This structure provides an abstract framework for homotopy theory.
    *   **Reference:** Quillen, D. (1967). *Homotopical Algebra*. Springer. Chapter I, Section 1.

*   **Simplicial model category**: A model category `M` that is enriched over the category of simplicial sets `sSet`, such that the enrichment is compatible with the model structure (the pushout-product axiom holds).
    *   **Reference:** Hovey, M. (1999). *Model Categories*. American Mathematical Society. Definition 4.2.1.

*   **Quillen adjunction**: An adjunction `F: C ⊣ G: D` between two model categories `C` and `D` such that `F` preserves cofibrations and trivial cofibrations, or equivalently, `G` preserves fibrations and trivial fibrations.
    *   **Reference:** Quillen, D. (1967). *Homotopical Algebra*. Springer. Chapter I, Section 4.

*   **Quillen equivalence**: A **Quillen adjunction** `F ⊣ G` that induces an equivalence between the homotopy categories `Ho(C) ≃ Ho(D)`. This is true if and only if for a cofibrant object `c` in `C` and a fibrant object `d` in `D`, a map `f: F(c) -> d` is a weak equivalence in `D` if and only if its adjunct `f̃: c -> G(d)` is a weak equivalence in `C`.
    *   **Reference:** Hovey, M. (1999). *Model Categories*. American Mathematical Society. Definition 1.3.12.

*   **Fibration in model categories**: One of the three distinguished classes of morphisms in a model category. Fibrations have the right lifting property with respect to trivial cofibrations (acyclic cofibrations). They are the abstract analogue of Serre fibrations in topology.
    *   **Reference:** Quillen, D. (1967). *Homotopical Algebra*. Springer. Chapter I, Section 1.

*   **Cofibration**: One of the three distinguished classes of morphisms in a model category. Cofibrations have the left lifting property with respect to trivial fibrations (acyclic fibrations). They are the abstract analogue of NDR-pairs in topology.
    *   **Reference:** Quillen, D. (1967). *Homotopical Algebra*. Springer. Chapter I, Section 1.

*   **Weak equivalence**: One of the three distinguished classes of morphisms in a model category. These are the morphisms that become isomorphisms in the homotopy category `Ho(C)`.
    *   **Reference:** Quillen, D. (1967). *Homotopical Algebra*. Springer. Chapter I, Section 1.

*   **Left Bousfield localization**: A process for creating a new model structure on a category `C` from an existing one by forcing a set of maps `S` to become weak equivalences. The new weak equivalences are the `S`-local equivalences, the cofibrations are the same, and the fibrations are modified to be the `S`-local fibrations.
    *   **Reference:** Hirschhorn, P. S. (2003). *Model Categories and Their Localizations*. American Mathematical Society. Chapter 3.

*   **Right Bousfield localization**: The dual process, where the fibrations are kept the same, the weak equivalences are modified, and the cofibrations are the maps with the left lifting property against the new trivial fibrations.
    *   **Reference:** Hirschhorn, P. S. (2003). *Model Categories and Their Localizations*. American Mathematical Society. Chapter 4.

*   **Monoidal model category**: A model category `C` that is also a monoidal category, where the monoidal product is compatible with the model structure (the pushout-product axiom holds).
    *   **Reference:** Hovey, M. (1999). *Model Categories*. American Mathematical Society. Definition 4.2.6.

*   **Enriched model category**: A model category `M` enriched over a monoidal model category `V`, with compatibility between the enrichment and the model structure. A simplicial model category is an example where `V = sSet`.
    *   **Reference:** Hovey, M. (1999). *Model Categories*. American Mathematical Society. Section 4.2.

*   **Relative category**: A category `C` equipped with a subcategory `W` of "weak equivalences". This is a minimal setting for abstract homotopy theory, a precursor to model categories. The homotopy category is formed by formally inverting the morphisms in `W`.
    *   **Reference:** Barwick, C., & Kan, D. M. (2012). *Relative categories: another model for the homotopy theory of homotopy theories*. Indagationes Mathematicae, 23(1-2), 42-68.

---

### Advanced Constructions

*   **Yoneda embedding for ∞-categories**: The ∞-categorical version of the Yoneda embedding. For an ∞-category `C`, it is the ∞-functor `y: C -> P(C) = Fun(C^op, S)`, where `S` is the ∞-category of spaces (∞-groupoids), that sends an object `c` to the representable presheaf `Map_C(-, c)`. This embedding is fully faithful.
    *   **Reference:** Lurie, J. (2009). *Higher Topos Theory*. Princeton University Press. Section 5.1.3.

*   **Grothendieck construction**: A construction that establishes an equivalence between fibrations `p: E -> B` over a category `B` and pseudofunctors `B -> Cat`. For an ∞-category `C`, the (∞-categorical) Grothendieck construction gives an equivalence between cocartesian fibrations `p: E -> C` and ∞-functors `C -> Cat_∞`.
    *   **Reference:** Lurie, J. (2009). *Higher Topos Theory*. Princeton University Press. Chapter 2 (for ∞-categories); Mac Lane, S., & Moerdijk, I. (1992). *Sheaves in Geometry and Logic*. Springer. Chapter I, Section 5 (for 1-categories).

*   **Straightening and unstraightening**: These are the names for the mutually inverse equivalences in the ∞-categorical Grothendieck construction. "Unstraightening" takes an ∞-functor `F: C -> Cat_∞` and produces a cocartesian fibration. "Straightening" is the inverse process.
    *   **Reference:** Lurie, J. (2009). *Higher Topos Theory*. Princeton University Press. Section 2.2.1.

*   **Factorization system**: See previous list.
    *   **Reference:** Borceux, F. (1994). *Handbook of Categorical Algebra 1: Basic Category Theory*. Cambridge University Press. Section 4.4.

*   **Orthogonal factorization system**: A factorization system `(E, M)` where `E` is the class of all morphisms left orthogonal to `M`, and `M` is the class of all morphisms right orthogonal to `E`.
    *   **Reference:** Adámek, J., Herrlich, H., & Strecker, G. E. (2004). *Abstract and Concrete Categories: The Joy of Cats*. Dover Publications. Section 14.

*   **Reflective subcategory**: See previous list.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter IV, Section 3.

*   **Coreflective subcategory**: See previous list.
    *   **Reference:** Adámek, J., Herrlich, H., & Strecker, G. E. (2004). *Abstract and Concrete Categories: The Joy of Cats*. Dover Publications. Chapter III, Section 10.

*   **Exact ∞-category**: An ∞-category with finite limits and a stable class of "exact sequences" satisfying axioms analogous to those of a Quillen exact category.
    *   **Reference:** Barwick, C. (2015). *On the exact-categories of K-theory*. Communications in Contemporary Mathematics, 17(03), 1450037.

*   **Stable ∞-category**: An ∞-category `C` that has a zero object, finite colimits and limits, and in which a square is a pushout if and only if it is a pullback. Equivalently, the suspension functor `Σ` is an equivalence. These are the ∞-categorical analogues of triangulated categories.
    *   **Reference:** Lurie, J. (2017). *Higher Algebra*. Available online from the author's website. Chapter 1.

*   **Presentable ∞-category**: An ∞-category `C` that is accessible and cocomplete. Equivalently, it is a localization of a presheaf ∞-category `P(K)` with respect to a set of morphisms. These are large but well-behaved ∞-categories.
    *   **Reference:** Lurie, J. (2009). *Higher Topos Theory*. Princeton University Press. Section 5.5.

*   **Accessible ∞-category**: An ∞-category `C` that has `κ`-filtered colimits for some regular cardinal `κ`, and is generated by a set of `κ`-presentable objects under `κ`-filtered colimits.
    *   **Reference:** Lurie, J. (2009). *Higher Topos Theory*. Princeton University Press. Section 5.4.

*   **Topos**: A category `E` that "behaves like the category of sheaves on a topological space". Formally, a topos is a category that is Cartesian closed and has a subobject classifier. A Grothendieck topos is a category equivalent to the category of sheaves on a site.
    *   **Reference:** Mac Lane, S., & Moerdijk, I. (1992). *Sheaves in Geometry and Logic: A First Introduction to Topos Theory*. Springer. Chapter IV.

*   **Higher topos**: A general term for an ∞-categorical version of a topos.
    *   **Reference:** Lurie, J. (2009). *Higher Topos Theory*. Princeton University Press.

*   **(∞,1)-topos**: An ∞-category `X` that satisfies the Giraud axioms for ∞-categories: it is presentable, colimits are universal, and groupoid objects are effective. They are precisely the left exact localizations of presheaf ∞-categories. They are the setting for ∞-stacks.
    *   **Reference:** Lurie, J. (2009). *Higher Topos Theory*. Princeton University Press. Chapter 6.

*   **(∞,n)-category**: A weak ∞-category where all `k`-morphisms for `k > n` are equivalences. An (∞,1)-category is the most studied case. An (∞,0)-category is an ∞-groupoid.
    *   **Reference:** Lurie, J. (2009). *On the classification of topological field theories*. In *Current Developments in Mathematics, 2008* (pp. 129-280). International Press.

*   **Cobordism hypothesis**: A theorem (due to Baez-Dolan, Lurie) that classifies fully extended topological quantum field theories (TQFTs). It states that the ∞-category of `n`-dimensional framed TQFTs is equivalent to the ∞-groupoid of fully dualizable objects in the target symmetric monoidal (∞,n)-category.
    *   **Reference:** Lurie, J. (2009). *On the classification of topological field theories*. In *Current Developments in Mathematics, 2008* (pp. 129-280). International Press.

*   **Day convolution**: A construction that endows a functor category `[C, V]` with a monoidal structure, provided `C` is a small monoidal category and `V` is a cocomplete closed monoidal category. The tensor product of two functors `F, G` is given by a coend formula: `(F * G)(c) = ∫^{c_1, c_2} F(c_1) ⊗ G(c_2) ⊗ C(c_1 ⊗ c_2, c)`.
    *   **Reference:** Day, B. J. (1970). *On closed categories of functors*. In *Reports of the Midwest Category Seminar IV* (pp. 1-38). Springer.

*   **Tannaka duality**: A class of theorems that reconstruct an algebraic group `G` from its category of representations `Rep(G)`. The category `Rep(G)` has a fiber functor to `Vect`, and `G` can be recovered as the automorphism group of this functor. This has been generalized to Tannakian categories.
    *   **Reference:** Deligne, P. (2007). *Catégories Tannakiennes*. In *The Grothendieck Festschrift, Volume 2* (pp. 111-195). Birkhäuser.

*   **Twisted arrow category**: For a category `C`, its twisted arrow category `Tw(C)` has morphisms of `C` as objects. A morphism from `f: A -> B` to `g: C -> D` is a pair of morphisms `(h: A -> C, k: B -> D)` such that `g ∘ h = k ∘ f`. It is used to model fibrations.
    *   **Reference:** Mac Lane, S., & Moerdijk, I. (1992). *Sheaves in Geometry and Logic*. Springer. Chapter I, Section 5.

---

### Dimensional Enhancements

*   **2-category**: A category enriched over **Cat**. It has objects, 1-morphisms, and 2-morphisms, and composition is strictly associative and unital.
    *   **Reference:** Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). Springer. Chapter XII, Section 1.

*   **3-category**: A category enriched over the category of 2-categories (**2-Cat**). It has cells up to dimension 3.
    *   **Reference:** Gordon, R., Power, A. J., & Street, R. (1995). *Coherence for tricategories*. Memoirs of the American Mathematical Society, 117(558).

*   **n-fold category**: An internal category in the category of `(n-1)`-fold categories. This gives `n` independent, commuting categorical structures on the same data.
    *   **Reference:** Brown, R., & Spencer, C. B. (1976). *G-groupoids, crossed modules and the fundamental groupoid of a topological group*. Indagationes Mathematicae, 38, 296-302.

*   **Iterated span category**: A category constructed by iterating the process of forming a category of spans.
    *   **Reference:** Morton, J. C. (2006). *A double bicategory of cobordisms with corners*. arXiv:math/0611930.

*   **Gray-category**: A category enriched over the category of 2-categories equipped with the Gray tensor product. This is a semi-strict model for a 3-category, where the interchange law holds only up to a coherent isomorphism.
    *   **Reference:** Gray, J. W. (1974). *Formal Category Theory: Adjointness for 2-Categories*. Springer.

*   **Trimble n-category**: A definition of a weak `n`-category proposed by Trimble, based on an operadic approach.
    *   **Reference:** Leinster, T. (2004). *Higher Operads, Higher Categories*. Cambridge University Press. Chapter 12.

*   **Tamsamani n-category**: A model for weak `n`-categories defined as certain Segal-type objects in the category of `(n-1)`-categories.
    *   **Reference:** Tamsamani, Z. (1999). *Sur les notions de n-catégorie et n-groupoïde non strictes via des ensembles multi-simpliciaux*. K-Theory, 16(1), 51-99.

*   **Street nerve**: A functor from the category of strict ω-categories to the category of simplicial sets, which is part of a chain of Quillen equivalences relating various models of ∞-categories.
    *   **Reference:** Street, R. (1987). *The algebra of oriented simplexes*. Journal of Pure and Applied Algebra, 49(3), 283-335.

*   **Θ-space**: A model for weak ∞-categories based on presheaves on a category `Θ` of decorated trees, developed by Joyal.
    *   **Reference:** Berger, C. (2002). *A cellular nerve for higher categories*. Advances in Mathematics, 169(1), 118-175.

*   **Rezk completion**: A procedure that turns a Segal space into a complete Segal space, which is a model for an (∞,1)-category.
    *   **Reference:** Rezk, C. (2001). *A model for the homotopy theory of homotopy theory*. Transactions of the American Mathematical Society, 353(3), 973-1007.

*   **Homotopy coherent nerve**: A functor from simplicially enriched categories to simplicial sets, which gives a model for the underlying (∞,1)-category. For a simplicially enriched category `C`, its nerve is `N_{hc}(C)_n = Hom_{sCat}(Δ[n], C)`.
    *   **Reference:** Lurie, J. (2009). *Higher Topos Theory*. Princeton University Press. Section 1.1.5.

*   **ω-category**: Another name for a strict ∞-category.
    *   **Reference:** Street, R. (1987). *The algebra of oriented simplexes*. Journal of Pure and Applied Algebra, 49(3), 283-335.

---

### Algebraic Geometry & Physics

*   **Derived stack**: A "space" that is locally modeled by derived affine schemes (spectra of simplicial commutative rings or connective E_∞-rings). It is an object in a higher topos, typically a sheaf of spaces on the site of commutative rings that satisfies a descent condition.
    *   **Reference:** Toën, B., & Vezzosi, G. (2005). *Homotopical Algebraic Geometry I: Topos theory*. Advances in Mathematics, 193(2), 257-372.

*   **Higher stack**: A stack whose values are not just groupoids, but `n`-groupoids or ∞-groupoids. An (∞,1)-topos is a category of ∞-stacks.
    *   **Reference:** Lurie, J. (2009). *Higher Topos Theory*. Princeton University Press. Section 6.1.

*   **Perfect stack**: A derived stack whose cotangent complex is a perfect complex. This is a strong finiteness condition.
    *   **Reference:** Ben-Zvi, D., Francis, J., & Nadler, D. (2010). *Integral transforms and Drinfeld centers in derived algebraic geometry*. Journal of the American Mathematical Society, 23(4), 909-966.

*   **Geometric Langlands program**: A reformulation of the Langlands correspondence in the language of algebraic geometry. It conjectures an equivalence of derived categories: the derived category of `D`-modules on the stack of `G`-bundles on a curve `X` should be equivalent to the derived category of coherent sheaves on the stack of `L_G`-local systems on `X`, where `L_G` is the Langlands dual group.
    *   **Reference:** Frenkel, E. (2007). *Lectures on the Langlands Program and Conformal Field Theory*. In *Frontiers in Number Theory, Physics, and Geometry II* (pp. 387-533). Springer.

*   **Topological field theory (TFT)**: A symmetric monoidal functor `Z: nCob -> Vect` from a category of `n`-dimensional cobordisms to the category of vector spaces. It assigns a vector space to each `(n-1)`-manifold and a linear map to each `n`-dimensional cobordism between them.
    *   **Reference:** Atiyah, M. (1988). *Topological quantum field theories*. Publications Mathématiques de l'IHÉS, 68, 175-186.

*   **Extended TQFT**: A TQFT that also assigns data to manifolds of lower dimensions. A fully extended `n`-dimensional TQFT is a symmetric monoidal ∞-functor from an (∞,n)-category of cobordisms `Bord_n` to a target symmetric monoidal (∞,n)-category.
    *   **Reference:** Baez, J. C., & Dolan, J. (1995). *Higher-dimensional algebra and topological quantum field theory*. Journal of Mathematical Physics, 36(11), 6073-6105.

*   **Conformal field theory (CFT)**: A quantum field theory that is invariant under conformal transformations. In 2D, the symmetry algebra is infinite-dimensional (the Virasoro algebra), leading to a rich mathematical structure.
    *   **Reference:** Di Francesco, P., Mathieu, P., & Sénéchal, D. (1997). *Conformal Field Theory*. Springer.

*   **Factorization algebra**: A mathematical structure that encodes the operator product expansion of a quantum field theory. It assigns a vector space (or chain complex) to each open set of a manifold and provides compatible multiplication maps for disjoint open sets contained in a larger one.
    *   **Reference:** Costello, K., & Gwilliam, O. (2017). *Factorization Algebras in Quantum Field Theory*. Cambridge University Press.

*   **Chiral algebra**: The algebraic structure that governs the holomorphic sector of a 2D CFT. It is a version of a factorization algebra on the complex line.
    *   **Reference:** Beilinson, A., & Drinfeld, V. (2004). *Chiral Algebras*. American Mathematical Society.

*   **Vertex operator algebra (VOA)**: An algebraic axiomatization of a chiral algebra in 2D CFT. It is a graded vector space with a state-field correspondence that assigns an operator-valued formal power series to each vector, satisfying certain axioms.
    *   **Reference:** Frenkel, I., Lepowsky, J., & Meurman, A. (1988). *Vertex Operator Algebras and the Monster*. Academic Press.

*   **Deformation quantization**: A procedure for constructing a quantum theory from a classical one. It deforms the commutative algebra of functions on a Poisson manifold into a non-commutative associative algebra (a "star product"), where the first-order term of the commutator is the Poisson bracket.
    *   **Reference:** Kontsevich, M. (2003). *Deformation quantization of Poisson manifolds*. Letters in Mathematical Physics, 66(3), 157-216.

*   **Drinfeld center**: For a monoidal category `C`, its Drinfeld center `Z(C)` is the category of objects `(X, β)` where `X` is an object of `C` and `β` is a "half-braiding" `β_Y: X ⊗ Y -> Y ⊗ X` which is natural in `Y`. The center `Z(C)` is always a braided monoidal category.
    *   **Reference:** Etingof, P., Gelaki, S., Nikshych, D., & Ostrik, V. (2015). *Tensor Categories*. American Mathematical Society. Section 7.13.

*   **Hochschild cohomology**: For an algebra `A` over a ring `k`, its Hochschild cohomology `HH^*(A, M)` with coefficients in an `A`-bimodule `M` is `Ext^*_{A-A}(A, M)`. It controls the deformations of the algebra `A`.
    *   **Reference:** Weibel, C. A. (1994). *An Introduction to Homological Algebra*. Cambridge University Press. Chapter 9.

*   **Cyclic homology**: A variant of Hochschild homology that incorporates a cyclic symmetry, related to K-theory and non-commutative geometry.
    *   **Reference:** Loday, J. L. (1998). *Cyclic Homology* (2nd ed.). Springer.

*   **A∞-algebra**: A "homotopy associative algebra". It is a graded vector space `A` with a sequence of multilinear maps `m_n: A^⊗n -> A` of degree `2-n` for `n ≥ 1`, satisfying a series of relations (the Stasheff identities) that generalize the associativity law up to a coherent system of homotopies.
    *   **Reference:** Stasheff, J. D. (1963). *Homotopy associativity of H-spaces. I, II*. Transactions of the American Mathematical Society, 108, 275-312.

*   **A∞-category**: A "homotopy category". It is a category enriched over chain complexes where the composition law is not strictly associative, but is associative up to a specified chain homotopy, which in turn satisfies higher coherence laws.
    *   **Reference:** Keller, B. (2001). *Introduction to A-infinity algebras and modules*. In *Homology, Homotopy and Applications*, 3(1), 1-35.

*   **L∞-algebra**: A "homotopy Lie algebra". It is a graded vector space `L` with a sequence of graded-antisymmetric multilinear maps `l_n: L^⊗n -> L` of degree `2-n` satisfying a sequence of relations that generalize the Jacobi identity up to coherent homotopy.
    *   **Reference:** Lada, T., & Stasheff, J. (1993). *Introduction to SH Lie algebras for physicists*. International Journal of Theoretical Physics, 32(7), 1087-1103.

*   **dg-category**: A category enriched over the category of chain complexes of abelian groups (or `k`-modules). Composition is associative and unital on the nose.
    *   **Reference:** Keller, B. (2006). *On differential graded categories*. In *International Congress of Mathematicians, Vol. II* (pp. 151-190). European Mathematical Society.

*   **Spectral category**: A category enriched over the monoidal category of spectra.
    *   **Reference:** Schwede, S., & Shipley, B. (2000). *Algebras and modules in monoidal model categories*. Proceedings of the London Mathematical Society, 80(2), 491-511.

*   **Shifted symplectic structure**: A generalization of a symplectic structure to derived algebraic geometry. A `k`-shifted symplectic structure on a derived stack `X` is a non-degenerate closed 2-form of degree `k` in the cotangent complex of `X`.
    *   **Reference:** Pantev, T., Toën, B., Vaquié, M., & Vezzosi, G. (2013). *Shifted symplectic structures*. Publications Mathématiques de l'IHÉS, 117(1), 271-328.

*   **Factorization homology**: A homology theory for manifolds with coefficients in an `E_n`-algebra. It is a way to "integrate" an algebraic structure over a manifold. For a manifold `M` and an `E_k`-algebra `A`, the factorization homology `∫_M A` is an `E_{n-k}`-algebra.
    *   **Reference:** Lurie, J. (2017). *Higher Algebra*. Available online from the author's website. Chapter 5.