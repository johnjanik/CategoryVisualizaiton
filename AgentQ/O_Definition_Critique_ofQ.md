Below I list the (few) items whose statements are **incomplete, slightly misleading, or use a non-standard formulation.**
Everything **not mentioned** passed a careful line-by-line check.  Where relevant I also give a *tight* textbook-style replacement.

| Entry                                      | Issue                                                                                                                                                                | Minimal correction / clarification                                                                                                                                                                                                           |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Abelian category**                       | Missing the *additive* hypothesis.  Having a zero object and binary (co)products does **not** force the hom-sets to be abelian groups or composition to be bilinear. | “An **abelian category** is an **additive** category with all kernels and cokernels in which every monomorphism is a kernel and every epimorphism is a cokernel.”  (Finite biproducts and a zero object come automatically from “additive”.) |
| **Cosegment**                              | Definition given is model–category-specific and not a standard categorical notion; readers might infer it is universally accepted.                                   | Preface with “*In the literature on simplicial model categories* a **cosegment** …” or drop the term unless you really need that specialised concept.                                                                                        |
| **Coefficient (enriched / hyperdoctrine)** | Too vague to count as a definition.                                                                                                                                  | Spell out the context: e.g. “In a **V**-enriched setting a *coefficient* object is an element of **V** that parametrises a family of predicates …”.  Otherwise remove.                                                                       |
| **Dinatural transformation**               | Only says “satisfies a coherence condition”.                                                                                                                         | Add the condition explicitly: for $F,G:\mathcal C^{\mathrm{op}}\!\times\!\mathcal C\to\mathcal D$,                                                                                                                                           |

$$
G(f,1)\,\alpha_c \;=\; \alpha_{c'}\,F(1,f)
\quad\text{for every }f:c\!\to c'.
\] |
| **Factorisation system** | “Orthogonal” is mentioned but the *unique lifting property* is what orthogonality means. | Append: “i.e. for every commutative square with the left map in \(\mathcal E\) and the right map in \(\mathcal M\) there exists a **unique** diagonal filler.” |
| **Grothendieck fibration** | Needs the *chosen lift* to be **cartesian** and stable under composition. | “…there exists a morphism \(\bar f:e'\to e\) over \(f\) such that every map over the composite factors *uniquely* through \(\bar f\); cartesian lifts are required to compose.” |
| **Locally presentable category** | Must involve a regular cardinal \(\lambda\). | “\(\mathcal C\) is **locally \(\lambda\)-presentable** if it is cocomplete and generated under \(\lambda\)-filtered colimits by a **set** of \(\lambda\)-presentable objects.  A category is *locally presentable* if this holds for *some* \(\lambda\).” |
| **Closed category** | Standard usage is *monoidal* closed.  The draft divorces the internal-hom from a tensor. | Replace by: “A **monoidal closed** category is a monoidal category \((\mathcal C,\otimes,I)\) in which each functor \(A\otimes-\) has a right adjoint \([A,-]\).” |
| **n-category** | In the weak case the cells above dimension \(n\) are *invertible*, not identity. | “…all \(k\)-morphisms for \(k>n\) are **invertible (or equivalences)**; in the **strict** variant they are strict identities.” |
| **Power (exponential)** | Minor slip: the representing functor is \(\mathcal C(S\cdot-,X)\), not \(\mathcal C(X,-)^S\). | “\(X^S\) represents \(\mathcal C(S\!\cdot\!-,X)\), i.e. \(\mathcal C(Y,X^S)\cong\mathrm{Set}(S,\mathcal C(Y,X))\).” |
| **Zero morphism** | Only defined via a zero **object**; many authors allow zero morphisms without a global zero object. | If you intend the stricter sense, keep as is; otherwise note the broader definition (“a morphism that factors through *some* zero object when it exists”). |

---

### Quick remarks on other small points

*  **Adjoint Functor Theorem** – the statement you gave is the *General* AFT for existence of **left** adjoints; there is a dual version for right adjoints (cocomplete + limit-preserving).  
*  **Exact category** – perfectly fine, but you could add “the conflations are closed under isomorphism, pushout and pullback along inflations/deflations.”  
*  **Cauchy (Karoubi) completion** – correct; worth adding that the inclusion \(\mathcal C\hookrightarrow\widehat{\mathcal C}\) is fully faithful and idempotent-complete.  
*  **Closed / compact / pivotal / fusion / modular** categories – all otherwise accurate.  
*  The duplicate entry **Multicategory** in the operad section is consistent with the earlier one.

If you need *full* polished textbook formulations for any of the items above—or for the Higher-Category list that follows—just let me know!
$$
