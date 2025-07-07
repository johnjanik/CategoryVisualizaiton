### Classical Category Theory

* **Abelian category** — An additive category $\mathcal{A}$ with finite limits and colimits such that every monomorphism is a kernel of some morphism and every epimorphism is a cokernel; equivalently, every morphism has an image and coimage and the canonical map coimage $\to$ image is an isomorphism.
* **Additive category** — A preadditive category that has a zero object and all finite biproducts, so that each Hom‑set is an abelian group and composition is bilinear.
* **Adjoint functor theorem** — A theorem giving sufficient conditions for a functor $F : \mathcal{C} \to \mathcal{D}$ to admit a right (resp. left) adjoint, typically that $F$ preserves limits (resp. colimits) of a certain shape and that the target category is complete (resp. cocomplete) and locally small plus a solution‑set condition.
* **Adjunction (unit, counit; left and right adjoints)** — An adjunction between categories $\mathcal{C}$ and $\mathcal{D}$ is a pair of functors $F : \mathcal{C} \leftrightarrows \mathcal{D} : G$ together with natural transformations (unit) $\eta : 1_\mathcal{C} \Rightarrow G F$ and (counit) $\varepsilon : F G \Rightarrow 1_\mathcal{D}$ satisfying the triangle identities; $F$ is the left adjoint and $G$ the right adjoint.
* **Automorphism** — An isomorphism from an object to itself in a category; i.e. a morphism $f : A \to A$ with a two‑sided inverse.
* **Balanced category** — A category in which every morphism that is both a monomorphism and an epimorphism is necessarily an isomorphism.
* **Category (small, large, locally small)** — A category is a collection of objects and morphisms between them with associative composition and identity morphisms; it is **small** if its class of objects forms a set, **large** if not, and **locally small** if each Hom‑class is a set.
* **Category of elements** — For a functor $F : \mathcal{C} \to \mathbf{Set}$ the category $\int_\mathcal{C} F$ whose objects are pairs $(C, x)$ with $C\in \mathcal{C}$ and $x\in F(C)$, and whose morphisms $(C,x)\to(D,y)$ are arrows $f:C\to D$ in \mathcal{C} such that $F(f)(x)=y$.
* **Cauchy (Karoubi) completion** — The completion of a category $\mathcal{C}$ obtained by formally splitting all idempotent endomorphisms; objects are idempotent pairs $(A,e)$ with $e^2=e:A\to A$.
* **Comma category** — Given functors $S:\mathcal{A}\to\mathcal{C}$ and $T:\mathcal{B}\to\mathcal{C}$, the category $(S\downarrow T)$ whose objects are triples $(A,B,f:S(A)\to T(B))$ and morphisms are pairs of morphisms in $\mathcal{A},\mathcal{B}$ making the evident square commute.
* **Composition (associativity, identity laws)** — For composable morphisms $f,g,h$ composition is a binary operation $\circ$ such that $h\circ(g\circ f)=(h\circ g)\circ f$ (associativity) and $1_B\circ f = f = f\circ 1_A$ for identities $1_A,1_B$.
* **Contravariant functor** — A mapping $F:\mathcal{C}^{op}\to\mathcal{D}$; it reverses the direction of morphisms.
* **Copower (tensoring with a set or object)** — For a category $\mathcal{C}$ enriched over $\mathbf{Set}$, the copower of an object $C$ by a set $I$ is the coproduct $\coprod_{i\in I} C$, denoted $I \cdot C$; dually in enriched settings $A\otimes X$.
* **Copresheaf** — A functor $\mathcal{C}\to\mathbf{Set}$; equivalently, a presheaf on the opposite category.
* **Coproduct** — A universal cocone under a family of objects, i.e. an object $C$ with injections $i_j:A_j\to C$ such that for any cocone there is a unique mediating morphism.
* **Cosegment** — For a category with finite coproducts, the initial object together with two coproduct injections $0\to 1\amalg1$; dually to segment.
* **Coslice category** — For an object $A$ in $\mathcal{C}$, the category $A/\mathcal{C}$ whose objects are morphisms $A\to X$ and morphisms are commutative triangles over $A$.
* **Coequalizer** — The universal arrow from a parallel pair $f,g:A\rightrightarrows B$; an object $Q$ with $q:B\to Q$ such that $q f = q g$ and universal with that property.
* **Coefficient (in enriched/hyperdoctrine contexts)** — An object or element used to weight an indexed tensor/hom, e.g. in a $V$-enriched category coefficients lie in $V$.
* **Coend** — For a functor $H:\mathcal{C}^{op}\times\mathcal{C}\to\mathcal{D}$, the coend $\int^{C} H(C,C)$ is the coequalizer of the pair built from $H$ acting on morphisms; it is the colimit that coequalizes left and right actions.
* **Coreflective subcategory** — A full subcategory $ \mathcal{A}\subseteq\mathcal{C}$ for which the inclusion has a right adjoint.
* **Covariant functor** — A functor $F:\mathcal{C}\to\mathcal{D}$ preserving the direction of morphisms.
* **Dinatural transformation** — A family $\phi_C:H(C,C)\to K(C,C)$ between functors $H,K:\mathcal{C}^{op}\times\mathcal{C}\to\mathcal{D}$ such that a certain hexagon identity holds for every morphism.
* **Dual category (opposite category)** — The category $\mathcal{C}^{op}$ with the same objects as $\mathcal{C}$ but morphisms reversed.
* **End** — For $H:\mathcal{C}^{op}\times\mathcal{C}\to\mathcal{D}$, the end $\int_{C} H(C,C)$ is the equalizer of the induced pair of morphisms; a limit dual to the coend.
* **Equalizer** — The universal arrow into a pair $f,g:A\rightrightarrows B$; an object $E$ with $e:E\to A$ such that $f e = g e$.
* **Essentially surjective functor** — A functor $F:\mathcal{C}\to\mathcal{D}$ such that every object of $\mathcal{D}$ is isomorphic to $F(C)$ for some $C$.
* **Exact category** — An additive category equipped with a class of “short exact sequences” satisfying axioms analogous to those in an abelian category (Quillen exact structure).
* **Factorization system** — A pair $(\mathcal{E},\mathcal{M})$ of classes of morphisms such that every morphism factors as $m\circ e$ with $e\in\mathcal{E}$, $m\in\mathcal{M}$, both classes are closed under composition with isomorphisms, and $\mathcal{E}$ morphisms are left orthogonal to $\mathcal{M}$ morphisms.
* **Fully faithful functor** — A functor inducing bijections on all Hom‑sets.
* **Functor (covariant, contravariant)** — A mapping between categories preserving composition and identities; covariant preserves direction, contravariant reverses.
* **Functor category** — For categories $\mathcal{C},\mathcal{D}$, the category $[\mathcal{C},\mathcal{D}]$ whose objects are functors and morphisms are natural transformations.
* **Full functor** — A functor that is surjective on each Hom‑set.
* **Grothendieck fibration** — A functor $p:\mathcal{E}\to\mathcal{B}$ such that for each $e\in\mathcal{E}$ and arrow $f:b\to p(e)$ in \mathcal{B} there exists a $p$-cartesian morphism over $f$.
* **Grothendieck topology** — For a small category $\mathcal{C}$, an assignment of covering sieves satisfying maximality, stability, and transitivity axioms, turning $\mathcal{C}$ into a site.
* **Image (regular image, categorical image)** — The factor $A\xrightarrow{e} \operatorname{im}(f)\xrightarrow{m} B$ of a morphism $f$ given by a (regular) epi‑mono factorization; if $\mathcal{C}$ has such factorization, $im(f)$ is the image.
* **Initial object** — An object $0$ such that for every object $A$ there exists a unique morphism $0\to A$.
* **Isomorphism** — A morphism $f:A\to B$ with an inverse $g:B\to A$ such that $gf=1_A$ and $fg=1_B$.
* **Kan extension (left and right)** — Given $F:\mathcal{A}\to\mathcal{C}$ and $K:\mathcal{A}\to\mathcal{B}$, the left Kan extension $Lan_K F:\mathcal{B}\to\mathcal{C}$ is universal among functors equipped with natural transformation $F \Rightarrow (Lan_K F)\circ K$; dually for right Kan extension $Ran_K F$.
* **Kernel** — The equalizer of a morphism with the zero morphism $f:A\to B$ in an additive category; $ker(f)\to A$.
* **Lawvere theory** — A small category with finite products whose objects are natural numbers $n$ and whose morphisms encode operations of an algebraic theory.
* **Limit (inverse limit, pullback, etc.)** — A universal cone over a diagram $D:\mathcal{J}\to\mathcal{C}$; an object $L$ with projections to $D$ such that any other cone factors uniquely.
* **Locally presentable category** — A cocomplete category that is generated under $\lambda$-filtered colimits by a set of $\lambda$-presentable objects for some regular cardinal $\lambda$.
* **Monomorphism** — A morphism $m:A\to B$ such that $m f = m g$ implies $f=g$ for all $f,g: X\to A$.
* **Multicategory** — A structure with objects and multimorphisms $f:(A_1,\dots,A_n)\to B$ with associative composition and identities, generalising both categories and operads.
* **Natural transformation (vertical/horizontal composition)** — Given functors $F,G:\mathcal{C}\to\mathcal{D}$, a family $\eta_A:F(A)\to G(A)$ natural in $A$; vertical composition composes natural transformations having same source and target, horizontal composition composes along functors.
* **Natural isomorphism** — A natural transformation each of whose components is an isomorphism.
* **Nerve of a category** — The simplicial set $N(\mathcal{C})_n = \mathrm{Fun}([n],\mathcal{C})$.
* **Opposite category** — Same as dual category.
* **Power (exponentials, internal homs)** — For objects $A,B$ in a cartesian closed category, the exponential $B^A$ equipped with an evaluation map universal for currying; more generally an internal hom $[A,B]$.
* **Preadditive category** — A category enriched in abelian groups; Hom‑sets are abelian groups and composition is bilinear.
* **Product** — A universal cone under a family of objects; dual to coproduct.
* **Pullback** — The limit of a cospan $A\xrightarrow{f} C \xleftarrow{g} B$; object $P$ with projections making square commute and universal.
* **Pushout** — The colimit of a span $A\xleftarrow{f} C \xrightarrow{g} B$.
* **Reflective subcategory** — A full subcategory whose inclusion has a left adjoint.
* **Representable functor** — A functor naturally isomorphic to $\mathcal{C}(A,-)$ for some $A$ (covariant) or $\mathcal{C}(-,A)$ (contravariant).
* **Retract (section/retraction)** — A morphism $s:A\to B$ with a right inverse $r:B\to A$ (i.e. $r s = 1_A$); $A$ is a retract of $B$.
* **Slice category** — For object $A$, the category $\mathcal{C}/A$ whose objects are morphisms $X\to A$.
* **Split exact sequence** — A short exact sequence that admits a splitting morphism equivalently is isomorphic to $A\oplus B$.
* **Split monomorphism / split epimorphism** — A mono $m$ that has a left inverse, or an epi $e$ with a right inverse.
* **Subobject** (subobject classifier in a topos) — An equivalence class of monomorphisms into $A$; in a topos classified by a morphism $A\to \Omega$.
* **Terminal object** — An object $1$ such that for every $A$ there is a unique morphism $A\to 1$.
* **Universal arrow / universal property** — An arrow exhibiting an adjunction; $u:C\to G A$ universal from $C$ to $G$ if every morphism $C\to G X$ factors uniquely through $u$.
* **Weak limit / weak colimit** — A cone (cocone) satisfying universality only up to (not necessarily unique) isomorphism.
* **Zero object** — An object that is both initial and terminal.
* **Zero morphism** — In a pointed category, a unique morphism $0_{A,B}:A\to B$ factoring through the zero object.

### Basic Higher Category Concepts

* **∗Complicial set** — A stratified simplicial set satisfying the complicial horn‑filling conditions modeling (∞,1)-categories à la Street.
* **Cellular set** — A presheaf on the category of globes giving a combinatorial model for strict $\omega$-categories.
* **Homotopy category** — For a model or ∞‑category $\mathcal{C}$, the ordinary category obtained by formally inverting weak equivalences (or equivalences).
* **n-category** — A category enriched in (n−1)-categories with morphisms defined up to dimension $n$; composition associative and unital at all levels.
* **∞-category** — A weak n‑category for all n; commonly modeled by quasicategories, complete Segal spaces, etc.
* **Weak n-category** — An n-category whose associativity and unit laws hold only up to coherent higher equivalences.
* **Strict n-category** — An n-category where all associativity/unit laws are strict equalities.
* **Bicategory** — A weak 2-category: objects, 1‑morphisms, 2‑morphisms with composition associative and unital up to coherent isomorphism.
* **Globular set** — A presheaf on the globe category giving the data for opetopic/higher categories.
* **Nerve of a category** — As above; embeds Cat into simplicial sets.
* **Quasicategory** — A simplicial set satisfying the inner horn‑filling condition; Joyal’s model for ∞‑categories.
* **Kan complex** — A simplicial set in which every horn has a filler; models ∞‑groupoids.
* **Simplicial set** — A presheaf on the simplex category $\Delta$.
* **Complete Segal space** — A simplicial space satisfying Segal and completeness conditions modeling ∞‑categories à la Rezk.
* **Segal category** — A simplicial object in sets satisfying Segal conditions but with discrete 0‑simplices.
* **Homotopy hypothesis** — The conjecture that ∞‑groupoids are equivalent to homotopy types of spaces.

### Types of Higher Categories

* **Cartesian closed category** — A category with finite products and exponentials.
* **Closed category** — A monoidal category $(\mathcal{C},\otimes,I)$ where each tensor functor $A\otimes-$ has a right adjoint.
* **Compact closed category** — A symmetric monoidal category in which every object has a dual with evaluation and coevaluation maps satisfying snake identities.
* **Double category** — A structure with objects, horizontal and vertical morphisms and squares (2‑cells) composing in two directions.
* **Enriched category** — A category whose Hom‑objects lie in a monoidal category $V$ and composition is given by the monoidal product.
* **Internal category** — A category object in some ambient category $\mathcal{E}$; objects and morphisms are objects of $\mathcal{E}$.
* **Monoidal category** — A category equipped with tensor product $\otimes$, unit object $I$, and associativity/unit isomorphisms satisfying coherence.
* **Braided monoidal category** — A monoidal category with a natural braiding $c_{A,B}:A\otimes B\to B\otimes A$ satisfying hexagon identities.
* **Monoidal ∞-category** — An ∞‑category equipped with an ∞‑operad map to $N(\mathbf{\Gamma})$ giving coherently associative tensor product.
* **Omega-category (ω-category)** — A weak n‑category for all finite n with coherences at every level.
* **Pivotal category** — A rigid monoidal category with a monoidal natural isomorphism between the identity and double dual functors.
* **Fusion category** — A semisimple rigid monoidal category with finitely many simple objects and simple unit over an algebraically closed field.
* **Modular tensor category** — A ribbon fusion category with non‑degenerate braiding (S‑matrix invertible).
* **Symmetric monoidal category** — A braided monoidal category whose braiding is involutive $c_{B,A}\circ c_{A,B}=1$.
* **Virtual double category** — A generalization of double categories allowing horizontal composition only up to equivalence.

### Morphisms & Cells

* **k-morphism** — A morphism of dimension $k$ in an $n$- or ∞‑category.
* **2-morphism** — A morphism between 1‑morphisms in a bicategory or 2‑category.
* **Higher morphism** — A morphism of dimension greater than 1.
* **Globular k-cell** — An element of a globular set of dimension k whose source and target are (k−1)-cells with parallel boundaries.
* **Icon** — A “2‑dimensional natural transformation” between lax functors that is identity on objects.
* **Lax natural transformation** — Between lax functors; components come with 2‑cells satisfying coherence.
* **Oplax natural transformation** — Dual to lax; 2‑cells oriented oppositely.
* **Pseudonatural transformation** — Between pseudofunctors; components are equivalences and satisfy pseudonaturality isomorphically.
* **Modification** — A 3‑cell between pseudonatural transformations in a bicategory.
* **Equivalence in higher categories** — A morphism admitting an inverse up to higher equivalences with associated coherence data.
* **Adjoint equivalence** — An equivalence equipped with specified unit and counit forming an adjunction whose triangle identities hold.

### Functors & Transformations

* **∞-functor** — A map of ∞‑categories preserving composition up to coherent homotopy.
* **Functor between bicategories** — A homomorphism (lax, pseudofunctor, or strict) preserving composition and identities up to coherent isomorphism.
* **Homotopy coherent diagram** — A functor defined up to specified homotopies encoding higher coherence relations.
* **Lax functor** — A functor between monoidal or higher categories preserving structure via specified comparison maps not necessarily invertible.
* **Oplax functor** — Dual to lax with comparisons reversed.
* **Pseudofunctor** — A lax functor whose comparison maps are invertible.
* **Transformation between ∞-functors** — A 1‑simplex in the mapping space between functors; higher cells give homotopies.
* **Natural isomorphism up to higher equivalence** — A natural transformation whose components are equivalences in an ∞‑category.

### Limits & Colimits

* **Homotopy colimit** — The ∞‑categorical colimit taken in a model of ∞‑categories ensuring correct homotopy type.
* **Homotopy limit** — The dual homotopy coherent limit.
* **∞-categorical colimit** — The universal object for cocones in an ∞‑category defined via mapping‑space equivalences.
* **∞-categorical limit** — The dual.
* **Weighted limit** — A limit defined with respect to a weight $W:\mathcal{J}\to \mathbf{Set}$ or $sSet$, generalizing ends.
* **Bicolimit** — A colimit in a bicategory universal up to equivalence.
* **Flexible limit** — A 2‑categorical limit computed by strict cones but universal only up to equivalence.
* **Kan extension in higher categories** — The ∞‑categorical generalization of Kan extensions using homotopy (co)limits.
* **Lax limit** — A limit defined via lax cones whose comparison maps need not be invertible.
* **Pseudolimit** — A bi‑limit whose universal property holds up to equivalence with invertible 2‑cells.
* **End (as a limiting construction)** — Same idea as classical end but enriched/higher; equalizer object of a diagram of mapping spaces.
* **Bilimit** — A limit in a bicategory universal up to equivalence with specified invertible modifications.

### Adjunctions & Duality

* **Adjunction in bicategories** — 1‑morphisms $f \dashv g$ with unit and counit 2‑cells satisfying triangle identities up to modification.
* **Biadjunction** — An adjunction internal to a tricategory (or between pseudofunctors).
* **Lax adjunction** — An adjunction where one leg is lax and the other oplax.
* **∞-adjunction** — An adjunction in an ∞‑category given by equivalence of mapping spaces.
* **Coend calculus** — Formal algebra of manipulating ends and coends (especially in enriched categories).
* **Dualizable object** — In a monoidal ∞‑category, an object admitting evaluation and coevaluation morphisms satisfying zig‑zag identities.
* **Fully dualizable object** — An object that is dualizable at every higher morphism level up to the dimension of interest.
* **Serre duality** — A duality between coherent sheaf cohomology groups on a smooth projective variety encoded by a canonical bundle.
* **Verdier duality** — The duality functor $D$ in derived category of sheaves relating proper pushforward and extraordinary pullback.
* **Grothendieck duality** — A general duality theorem for derived categories of coherent sheaves over morphisms of schemes.

### Monads & Algebras

* **Monad in a bicategory** — A 1‑endomorphism equipped with multiplication and unit 2‑cells satisfying associativity/unit laws.
* **Comonad** — Dual notion.
* **Eilenberg–Moore object** — A universal object classifying algebras over a monad in a bicategory.
* **Kleisli object** — Dually classifies free algebras.
* **Distributive law** — A 2‑cell between monads enabling their composite to be a monad.
* **Algebras for a monad** — Objects equipped with an action of the monad satisfying associativity/unit.
* **Coalgebras** — Dual.
* **Monadic functor** — A functor equivalent to the forgetful functor from Eilenberg–Moore category of some monad.
* **Barr–Beck theorem** — Gives necessary and sufficient conditions for a functor to be monadic.
* **Lax algebra** — An algebra for a monad where structure maps are not necessarily invertible.
* **Pseudo-monad** — A monad in a bicategory whose multiplication and unit are equivalences.
* **Pseudo-algebra** — An algebra for a pseudo‑monad with structure maps invertible up to higher cells.

### Operads & Algebraic Structures

* **Operad** — A collection $O(n)$ with symmetric group actions and composition maps governing n‑ary operations.
* **Multicategory** — As earlier.
* **PROP** — A symmetric strict monoidal category whose objects are natural numbers and morphisms model operations with multiple inputs/outputs.
* **Lawvere theory** — As earlier.
* **Topological operad** — Operad internal to topological spaces.
* **Symmetric operad** — Operad with full symmetric group action.
* **Cyclic operad** — Operad with invariance under cyclic permutations.
* **Modular operad** — Operad allowing connected graphs with loops.
* **Algebra over an operad** — An object with an action of the operad interpreting operations as maps.
* **Coalgebra over an operad** — Dual.
* **∞-operad** — Operad defined in ∞‑categorical context; e.g. Lurie’s ∞‑operads.
* **Dendroidal set** — A presheaf on the dendroidal category modeling ∞‑operads.
* **Colored operad** — Operad with multiple object colors; operations have inputs/outputs of specified colors.
* **Properad** — Generalization of operad allowing multiple inputs and outputs.
* **∞-properad** — Higher categorical version modeled by dendroidal objects.

### Topology & Homotopy Theory

* **Classifying space** — For a category or group $G$ the geometric realization $B G$ classifying principal $G$-bundles.
* **Delooping** — An iterative construction $B^n X$ such that $\Omega B X \simeq X$.
* **Loop space** — The space $\Omega X = \mathrm{Map}(S^1,X)$.
* **Loop space object** — In a pointed ∞‑category, an object $\Omega X$ with universal property of the loop functor.
* **Mapping space** — The hom‑object $\mathrm{Map}(A,B)$ in an ∞‑category, usually a Kan complex.
* **Fundamental ∞-groupoid** — The ∞‑groupoid of paths in a space; modelled by its singular complex.
* **Homotopy fiber** — The ∞‑categorical fiber of a map, given by the pullback along a path object.
* **Homotopy n-type** — A space whose homotopy groups vanish above dimension $n$.
* **Homotopy quotient** — The homotopy colimit of an action, $X//G$.
* **Stabilization** — Passage from spaces to spectra by formally inverting suspension.
* **Suspension** — The cofiber $Σ X = S^1 \wedge X$.

### Model Structures

* **Model category** — A category equipped with three classes of morphisms (cofibrations, fibrations, weak equivalences) satisfying Quillen’s axioms.
* **Simplicial model category** — A model category enriched over simplicial sets with compatible model structure.
* **Quillen adjunction** — An adjunction between model categories with left adjoint preserving cofibrations and trivial cofibrations.
* **Quillen equivalence** — A Quillen adjunction inducing equivalence on homotopy categories.
* **Fibration in model categories** — A morphism with right lifting property with respect to trivial cofibrations.
* **Cofibration** — Dually, left lifting property with respect to trivial fibrations.
* **Weak equivalence** — A morphism inverted in the homotopy category.
* **Left Bousfield localization** — A new model structure obtained by enlarging weak equivalences to kill a chosen set of maps.
* **Right Bousfield localization** — Dual.
* **Monoidal model category** — A monoidal category whose tensor product interacts suitably with model structure.
* **Enriched model category** — A model category enriched in a monoidal model category with compatibilities.
* **Relative category** — A pair $(\mathcal{C},\mathcal{W})$ of a category and a subcategory of weak equivalences.

### Advanced Constructions

| **Yoneda embedding for ∞-categories** | For a small ∞-category $\mathcal{C}$, the fully faithful functor $y \colon \mathcal{C} \to \mathrm{P}(\mathcal{C}) := \mathrm{Fun}(\mathcal{C}^{\mathrm{op}},\mathcal{S})$ sending an object $c$ to the *representable* presheaf $\operatorname{Map}_{\mathcal{C}}(-,c)$; here $\mathcal{S}$ is the ∞-category of spaces.                                                                          |
| **Grothendieck construction**         | The equivalence between (i) functors $F \colon \mathcal{C}^{\mathrm{op}}\to \mathbf{Cat}_{\infty}$ and (ii) (co)cartesian fibrations $p\colon\int_{\mathcal{C}}F\to\mathcal{C}$, given by taking the *category of elements* $\int_{\mathcal{C}}F$.                                                                                                                                                 |
| **Straightening & unstraightening**   | The Quillen equivalence $\mathrm{St},\mathrm{Un}$ between the model category of simplicial sets over $\mathrm{N}(\mathcal{C})$ with the Joyal model structure and the model category of functors $\mathrm{Fun}(\mathcal{C}^{\mathrm{op}},\mathbf{sSet}_{\mathrm{Joyal}})$; in ∞-categorical terms, an equivalence between cartesian fibrations over $\mathcal{C}$ and presheaves on $\mathcal{C}$. |
| **Factorization system**              | A pair $(E,M)$ of classes of morphisms in an ∞-category such that: (i) every arrow factors as $f= m\circ e$ with $ e\in E,\; m\in M$; (ii) $E$ is left orthogonal to $M$ (the mapping space $\operatorname{Map}(e,m)$ is contractible); (iii) both $E$ and $M$ are closed under retracts.                                                                                                          |
| **Orthogonal factorization system**   | A factorization system $(E,M)$ satisfying the stronger *unique-lifting* condition: for any square with $e\in E,\;m\in M$ there exists a *unique* filler up to contractible choice.                                                                                                                                                                                                                 |
| **Reflective subcategory**            | A full sub-∞-category $\mathcal{A}\subset\mathcal{C}$ such that the inclusion $i$ admits a **left** adjoint $L \colon \mathcal{C}\to\mathcal{A}$ (objects are *local*).                                                                                                                                                                                                                            |
| **Coreflective subcategory**          | Dually, a full sub-∞-category whose inclusion has a **right** adjoint.                                                                                                                                                                                                                                                                                                                             |
| **Exact ∞-category**                  | (Barwick) An additive ∞-category equipped with a class of “cofiber–fiber” sequences satisfying axioms generalising Quillen’s exact categories; yields a Waldhausen structure and K-theory.                                                                                                                                                                                                         |
| **Stable ∞-category**                 | A pointed ∞-category with finite limits and colimits in which the suspension functor $\Sigma$ (cofiber of the identity) is an equivalence; equivalently, pullbacks = pushouts.                                                                                                                                                                                                                     |
| **Presentable ∞-category**            | An ∞-category that is *accessible* (admits κ-filtered colimits and is generated under them by κ-compact objects for some regular κ) and admits **all** small colimits.                                                                                                                                                                                                                             |
| **Accessible ∞-category**             | An ∞-category admitting κ-filtered colimits for some κ and generated under those colimits by a small subcategory of κ-compact objects.                                                                                                                                                                                                                                                             |
| **Topos**                             | An elementary 1-category that is finitely complete, has all small colimits, is locally cartesian closed, and possesses a subobject classifier.                                                                                                                                                                                                                                                     |
| **Higher topos / (∞,1)-topos**        | A presentable ∞-category with finite limits whose colimits are *van Kampen* (i.e. preserved by pullback), equivalent to a left exact reflective localization of presheaves of spaces.                                                                                                                                                                                                              |
| **(∞,n)-category**                    | A weak higher category whose morphisms are defined up to level $n$ non-invertibly and become invertible above level $n$; formalized by complete Segal $\Theta_n$-spaces or other equivalent models.                                                                                                                                                                                                |
| **Cobordism hypothesis**              | In a symmetric monoidal $(\infty,n)$-category $\mathcal{C}$, fully extended framed $n$-dimensional TQFTs are classified (up to equivalence) by **fully dualizable** objects of $\mathcal{C}$; orientation/structure variants follow by adding tangential structure.                                                                                                                                |
| **Day convolution**                   | Given a small monoidal $\mathcal{C}$, the presheaf ∞-category $\mathrm{P}(\mathcal{C})$ inherits a closed monoidal structure whose tensor satisfies $(F\star G)(c)\simeq\int^{x,y} \mathcal{C}(x\otimes y,c)\times F(x)\times G(y)$.                                                                                                                                                               |
| **Tannaka duality**                   | The reconstruction of a (pro-)algebraic group / Hopf algebra (or higher-group stack) from its symmetric monoidal ∞-category of finite-type representations; formalised via fiber functors and recognition theorems.                                                                                                                                                                                |
| **Twisted arrow category**            | For a 1-category $\mathcal{C}$, $\mathrm{Tw}(\mathcal{C})$ has objects the morphisms $f\colon x\to y$; a map $(f\colon x\to y)\to(g\colon x'\to y')$ is a commutative square $x\xrightarrow{u}x',\;y\xleftarrow{v}y'$ with $g\circ u = v\circ f$.  In the ∞-context replace squares by homotopy-commuting 2-simplices.     

| Term                        | Definition                                                                                                                                                                                          |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2-category**              | A category enriched in **Cat**: objects, 1-morphisms, and 2-morphisms with vertical & horizontal composition, associative and unital up to strict equalities.                                       |
| **3-category**              | Category enriched in 2-Cat (objects, 1-, 2-, 3-morphisms) strictly associative/unital in every dimension.                                                                                           |
| **n-fold category**         | Iterated internal category in **Set** $n$ times; equivalently a functor $\Delta^{\mathrm{op}}\times\cdots\times\Delta^{\mathrm{op}}\to\mathbf{Set}$ satisfying Segal conditions in each coordinate. |
| **Iterated span category**  | For a base ∞-category with pullbacks, objects are the same, 1-morphisms are spans, 2-morphisms are spans of spans, etc.; composition via pullback.                                                  |
| **Gray-category**           | A *semi-strict* 3-category where interchange between 2-cells is controlled by the Gray tensor product—not symmetric—giving the enrichment used for tricategories.                                   |
| **Trimble n-category**      | Inductively defined weak $n$-categories built on topological operads, ensuring coherence by *contractible* operadic actions.                                                                        |
| **Tamsamani n-category**    | Weak $n$-category modelled as a simplicial index of $(n-1)$-categories satisfying Segal and globularity conditions; yields ($n,1$)-Segal spaces for $n\to\infty$.                                   |
| **Street nerve**            | The fully faithful functor $N_{\mathrm{str}}\colon \mathbf{2\,Cat}\to \mathbf{sSet}$ sending a 2-category to its Duskin nerve; generalises the classical nerve to 2-dimensions.                     |
| **Θ-space**                 | A presheaf on the Joyal cell category $\Theta$ satisfying Rezk’s completeness & Segal conditions; models $(\infty,n)$-categories.                                                                   |
| **Rezk completion**         | For a Segal space $X$, the fibrant replacement $X^\natural$ making $(\infty,1)$-equivalences invertible; universal with respect to being a **complete** Segal space.                                |
| **Homotopy coherent nerve** | Functor $\mathcal{N}_{\mathrm{hc}}\colon \mathbf{sSet}^{\Delta^{\mathrm{op}}}\to \mathbf{sSet}$ that sends a simplicial category to a quasicategory encoding coherent composition data.             |
| **ω-category (omega)**      | A strict higher category with $k$-morphisms for every $k\ge 0$ and strictly associative/unital composition along each dimension.                                                                    |

| Term                               | Definition                                                                                                                                                                                                                                      |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Derived stack**                  | A sheaf of ∞-groupoids on the site of simplicial commutative rings (or cdgas) that is *geometric* in the derived sense (admits an atlas by derived affines).                                                                                    |
| **Higher stack**                   | A stack of $(\infty,1)$-groupoids on a Grothendieck site, i.e. a presheaf of spaces satisfying descent for all coverings.                                                                                                                       |
| **Perfect stack**                  | A higher (or derived) stack whose (derived) category of quasi-coherent sheaves is compactly generated by perfect complexes; key in spectral algebraic geometry.                                                                                 |
| **Geometric Langlands program**    | Conjectural correspondence between $D$-modules on Bun$_G$ over a curve and quasi-coherent sheaves on the moduli stack of $\check G$-local systems, phrased in the language of ∞-categories and derived algebraic geometry.                      |
| **Topological field theory (TFT)** | A symmetric monoidal functor $Z\colon \mathbf{Cob}_{d}^{\mathrm{fr}}\to \mathcal{C}$ from a $d$-dimensional cobordism category to a symmetric monoidal target, invariant under diffeomorphisms.                                                 |
| **Extended TQFT**                  | A TFT valued in a symmetric monoidal $(\infty,n)$-category defined on manifolds with corners of all codimensions ≤ n, obeying higher gluing laws.                                                                                               |
| **Conformal field theory (CFT)**   | A 2-dimensional QFT whose correlation functions are invariant under conformal maps; mathematically encoded by a symmetric monoidal functor from a Segal modular functor category to **Vect**.                                                   |
| **Factorization algebra**          | A prefactorization cosheaf $\mathcal{F}$ on a manifold that is locally constant and satisfies *factorization*: $\mathcal{F}(U_1\sqcup\cdots\sqcup U_n)\simeq \bigotimes_i \mathcal{F}(U_i)$ for disjoint opens.                                 |
| **Chiral algebra**                 | A sheaf of Lie algebras on a curve equipped with a *chiral* (vertex-like) operation arising as the left chiral half of a CFT; formalised by Beilinson–Drinfeld.                                                                                 |
| **Vertex operator algebra (VOA)**  | A graded vector space with a state–field correspondence $Y(-,z)$, vacuum, and conformal vector satisfying Borcherds’ axioms; provides algebraic models of 2-D CFTs.                                                                             |
| **Deformation quantization**       | Given a Poisson manifold $(M,\{\, , \,\})$, an associative $ \mathbb{C}[[\hbar]]$-algebra structure on $ C^\infty(M)[[\hbar]]$ whose commutator reproduces $ \hbar\{\, , \,\}+O(\hbar^2)$.                                                      |
| **Drinfeld center**                | For a monoidal ∞-category $\mathcal{C}$, $\mathcal{Z}(\mathcal{C}) = \mathrm{Fun}_{\mathcal{C}\text{-}\mathcal{C}}(\mathcal{C},\mathcal{C})$ (bimodule endofunctors) inheriting a braided monoidal structure; classifies *commutative* objects. |
| **Hochschild cohomology**          | For an associative algebra $A$, $HH^{*}(A) = \operatorname{Ext}_{A^{e}}^{*}(A,A)$; for ∞-categories use $\operatorname{End}_{\mathrm{Fun}(A,A)}(\mathrm{Id})$; controls deformations.                                                           |
| **Cyclic homology**                | Periodic version of Hochschild homology accounting for cyclic symmetry: $HC_{*}(A) = HH_{*}(A)^{S^1}$.                                                                                                                                          |
| **$A_\infty$-algebra**             | A graded object with multiplications $m_k\colon A^{\otimes k}\to A[2-k]$ satisfying the Stasheff $A_\infty$-relations $\sum (-1)^{\epsilon} m_{r+1+t}(1^{\otimes r}\otimes m_s\otimes1^{\otimes t})=0$.                                         |
| **$A_\infty$-category**            | Category enriched in complexes where each hom-space is an $A_\infty$-algebra and composition is $A_\infty$ coherent.                                                                                                                            |
| **$L_\infty$-algebra**             | A graded Lie-type structure with brackets $\ell_k \colon \wedge^k V \to V[2-k]$ satisfying homotopy-Jacobi identities (codifferential squares to zero on cofree cocommutative coalgebra).                                                       |
| **dg-category**                    | A category enriched in chain complexes of $k$-modules; composition is a chain-map and associativity/unitality hold on the nose.                                                                                                                 |
| **Spectral category**              | Category enriched in spectra (a stable homotopy-theoretic refinement of dg-categories).                                                                                                                                                         |
| **Shifted symplectic structure**   | On a derived stack $X$, a closed, non-degenerate 2-form $\omega$ of cohomological degree $n$ (hence “$n$-shifted”), giving an equivalence between $\mathbb{T}_X[-n]$ and $\mathbb{L}_X$.                                                        |
| **Factorization homology**         | For an $E_n$-algebra $A$ and $n$-manifold $M$, the colimit $\int_M A$ over embeddings of disks into $M$ weighted by $A$; satisfies excision and recovers ordinary homology when $n=1$.                                                          |
