import networkx as nx

results = {}

# Define color codes for easier use
RED = "❌"
ORANGE = "⚠️"
YELLOW = "🟡"
GREEN = "✅"
N_A = "N/A"

# --- 1. Abelian category ---
# Defined by AgentD, AgentO, AgentQ, AgentC, AgentG
results["Abelian category"] = {
    "AgentD": {
        "Reviewer C": GREEN, # No specific critique found for DS.
        "Reviewer D": GREEN, # No specific critique found for DS.
        "Reviewer G": GREEN, # Listed as Accurate for DS.
        "Reviewer O": GREEN, # No specific critique found for DS.
        "Reviewer Q": GREEN, # No specific critique found for DS.
    },
    "AgentO": {
        "Reviewer C": GREEN, # No specific critique found for O.
        "Reviewer D": GREEN, # Listed as Correct for O.
        "Reviewer G": GREEN, # Listed as Accurate for O.
        "Reviewer O": GREEN, # No specific critique found.
        "Reviewer Q": GREEN, # Listed as Accurate for O.
    },
    "AgentQ": {
        "Reviewer C": GREEN, # No specific critique found for Q.
        "Reviewer D": GREEN, # Listed as Correct for Q.
        "Reviewer G": GREEN, # Listed as Correct for Q.
        "Reviewer O": ORANGE, # "Missing the additive hypothesis. Having a zero object and binary (co)products does **not** force the hom-sets to be abelian groups or composition to be bilinear." for Q.
        "Reviewer Q": GREEN, # Self-review lists as Accurate for Q.
    },
    "AgentC": {
        "Reviewer C": GREEN, # No self-critique found for C.
        "Reviewer D": GREEN, # Listed as Correct for C.
        "Reviewer G": GREEN, # Listed as Accurate for C.
        "Reviewer O": ORANGE, # "Minor note... you might simply remark that 'an abelian category is an additive category with all kernels and cokernels in which every mono and epi is normal (i.e.\ mono = kernel, epi = cokernel).'" for C.
        "Reviewer Q": GREEN, # Listed as Correct for C.
    },
    "AgentG": {
        "Reviewer C": GREEN, # No specific critique found for G.
        "Reviewer D": GREEN, # Listed as Correct for G.
        "Reviewer G": GREEN, # Self-review lists as Accurate for G.
        "Reviewer O": GREEN, # Listed as Accurate for G.
        "Reviewer Q": GREEN, # Listed as Correct for G.
    },
}

# --- 2. Adjoint functor theorem ---
# Defined by AgentD, AgentO, AgentQ, AgentC, AgentG
results["Adjoint functor theorem"] = {
    "AgentD": {
        "Reviewer C": GREEN, # No specific critique found for DS.
        "Reviewer D": GREEN, # No specific critique found for DS.
        "Reviewer G": GREEN, # Listed as Accurate for DS.
        "Reviewer O": GREEN, # No specific critique found for DS.
        "Reviewer Q": GREEN, # No specific critique found for DS.
    },
    "AgentO": {
        "Reviewer C": GREEN, # No specific critique found for O.
        "Reviewer D": GREEN, # Listed as Correct for O.
        "Reviewer G": GREEN, # Listed as Accurate for O.
        "Reviewer O": GREEN, # No specific critique found.
        "Reviewer Q": GREEN, # Listed as Accurate for O.
    },
    "AgentQ": {
        "Reviewer C": GREEN, # No specific critique found for Q.
        "Reviewer D": GREEN, # Listed as Correct for Q.
        "Reviewer G": RED, # Missing important technical conditions for Q.
        "Reviewer O": RED, # Missing important technical conditions for Q.
        "Reviewer Q": GREEN, # Self-review lists as Accurate for Q.
    },
    "AgentC": {
        "Reviewer C": GREEN, # No specific critique found for C.
        "Reviewer D": GREEN, # Listed as Correct for C.
        "Reviewer G": RED, # Missing hypotheses for C.
        "Reviewer O": RED, # Missing hypotheses for C.
        "Reviewer Q": GREEN, # No specific critique found for C.
    },
    "AgentG": {
        "Reviewer C": GREEN, # No specific critique found for G.
        "Reviewer D": GREEN, # Listed as Correct for G.
        "Reviewer G": GREEN, # Self-review lists as Correct for G.
        "Reviewer O": RED, # Missing important technical conditions for G.
        "Reviewer Q": RED, # Missing important technical conditions for G.
    },
}

# --- 3. Bilimit ---
# Defined by AgentD, AgentC, AgentQ, AgentG. AgentO does not explicitly define it in the provided sources.
results["Bilimit"] = {
    "AgentD": {
        "Reviewer C": GREEN, # No specific critique found for DS.
        "Reviewer D": GREEN, # No specific critique found for DS.
        "Reviewer G": RED, # "Incorrect identification of bilimit as synonym for bicolimit." for DS.
        "Reviewer O": GREEN, # No specific critique found for DS.
        "Reviewer Q": GREEN, # No specific critique found for DS.
    },
    "AgentO": {
        "Reviewer C": N_A,
        "Reviewer D": N_A,
        "Reviewer G": N_A,
        "Reviewer O": N_A,
        "Reviewer Q": N_A,
    },
    "AgentQ": {
        "Reviewer C": GREEN, # No specific critique found for Q.
        "Reviewer D": GREEN, # Listed as Correct for Q.
        "Reviewer G": GREEN, # No specific critique found for Q.
        "Reviewer O": GREEN, # No specific critique found for Q.
        "Reviewer Q": GREEN, # Self-review lists as Correct for Q.
    },
    "AgentC": {
        "Reviewer C": GREEN, # No specific critique found for C.
        "Reviewer D": GREEN, # Listed as Correct for C.
        "Reviewer G": GREEN, # Listed as Accurate for C.
        "Reviewer O": GREEN, # No specific critique found for C.
        "Reviewer Q": GREEN, # No specific critique found for C.
    },
    "AgentG": {
        "Reviewer C": GREEN, # No specific critique found for G.
        "Reviewer D": GREEN, # Listed as Correct for G.
        "Reviewer G": GREEN, # Self-review lists as Accurate for G.
        "Reviewer O": GREEN, # No specific critique found for G.
        "Reviewer Q": GREEN, # No specific critique found for G.
    },
}

# --- 4. Bicolimit ---
# Defined by AgentC, AgentG. Assumed N/A for AgentD, AgentO, AgentQ based on provided sources.
results["Bicolimit"] = {
    "AgentD": {
        "Reviewer C": N_A,
        "Reviewer D": N_A,
        "Reviewer G": N_A,
        "Reviewer O": N_A,
        "Reviewer Q": N_A,
    },
    "AgentO": {
        "Reviewer C": N_A,
        "Reviewer D": N_A,
        "Reviewer G": N_A,
        "Reviewer O": N_A,
        "Reviewer Q": N_A,
    },
    "AgentQ": {
        "Reviewer C": N_A,
        "Reviewer D": N_A,
        "Reviewer G": N_A,
        "Reviewer O": N_A,
        "Reviewer Q": N_A,
    },
    "AgentC": {
        "Reviewer C": GREEN, # No specific critique found for C.
        "Reviewer D": GREEN, # Listed as Correct for C.
        "Reviewer G": GREEN, # Listed as Accurate for C.
        "Reviewer O": GREEN, # No specific critique found for C.
        "Reviewer Q": GREEN, # No specific critique found for C.
    },
    "AgentG": {
        "Reviewer C": GREEN, # No specific critique found for G.
        "Reviewer D": GREEN, # Listed as Correct for G.
        "Reviewer G": GREEN, # Self-review lists as Accurate for G.
        "Reviewer O": GREEN, # Listed as Accurate for G.
        "Reviewer Q": GREEN, # No specific critique found for G.
    },
}

# --- 5. Cellular Set ---
# Defined by AgentO, AgentC, AgentG, AgentQ. AgentD does not define it.
results["Cellular Set"] = {
    "AgentD": {
        "Reviewer C": N_A,
        "Reviewer D": N_A,
        "Reviewer G": N_A,
        "Reviewer O": N_A,
        "Reviewer Q": N_A,
    },
    "AgentO": {
        "Reviewer C": GREEN, # No specific critique found for O.
        "Reviewer D": ORANGE, # "Likely typo; should be 'globular set'" for O.
        "Reviewer G": GREEN, # No specific critique found for O.
        "Reviewer O": ORANGE, # "This is likely a typo for **Globular Set**" for O (from overall summary).
        "Reviewer Q": GREEN, # No specific critique found for O.
    },
    "AgentQ": {
        "Reviewer C": GREEN, # No specific critique found for Q.
        "Reviewer D": GREEN, # Listed as Correct for Q.
        "Reviewer G": GREEN, # No specific critique found for Q.
        "Reviewer O": GREEN, # No specific critique found for Q.
        "Reviewer Q": GREEN, # Self-review lists as Correct for Q.
    },
    "AgentC": {
        "Reviewer C": GREEN, # No self-critique found for C.
        "Reviewer D": GREEN, # Listed as Correct for C.
        "Reviewer G": RED, # "Incorrect: This is not the standard definition of a cellular set... The definition provided seems to be for a **Theta-space** ... not a cellular set" for C.
        "Reviewer O": GREEN, # No specific critique found for C.
        "Reviewer Q": GREEN, # No specific critique found for C.
    },
    "AgentG": {
        "Reviewer C": GREEN, # No specific critique found for G.
        "Reviewer D": ORANGE, # "Non-standard; replace with *globular set*" for G.
        "Reviewer G": GREEN, # Self-review lists it as a `Cellular set` in Basic Higher Cat..
        "Reviewer O": GREEN, # No specific critique found for G.
        "Reviewer Q": GREEN, # No specific critique found for G.
    },
}

# --- 6. Category of elements ---
# Defined by AgentD, AgentO, AgentQ, AgentC, AgentG
results["Category of elements"] = {
    "AgentD": {
        "Reviewer C": GREEN, # Critique mentions it's a special case of Grothendieck construction but doesn't flag as error.
        "Reviewer D": GREEN, # No specific critique found for DS.
        "Reviewer G": GREEN, # Listed as Accurate for DS.
        "Reviewer O": RED, # "The arrow‐condition is reversed. Fix: A morphism... is f:c→c' **such that** F(f)(x)=x', not F(f)(x')=x." for DS.
        "Reviewer Q": GREEN, # No specific critique found for DS.
    },
    "AgentO": {
        "Reviewer C": GREEN, # No specific critique found for O.
        "Reviewer D": GREEN, # Listed as Correct for O.
        "Reviewer G": GREEN, # Listed as Accurate for O.
        "Reviewer O": GREEN, # No specific critique found.
        "Reviewer Q": GREEN, # Listed as Accurate for O.
    },
    "AgentQ": {
        "Reviewer C": GREEN, # No specific critique found for Q.
        "Reviewer D": GREEN, # Listed as Correct for Q.
        "Reviewer G": GREEN, # No specific critique found for Q.
        "Reviewer O": GREEN, # No specific critique found for Q.
        "Reviewer Q": GREEN, # Self-review lists as Correct for Q.
    },
    "AgentC": {
        "Reviewer C": GREEN, # No self-critique found for C.
        "Reviewer D": GREEN, # Listed as Correct for C.
        "Reviewer G": GREEN, # Listed as Accurate for C.
        "Reviewer O": GREEN, # Listed as Correct for C.
        "Reviewer Q": GREEN, # No specific critique found for C.
    },
    "AgentG": {
        "Reviewer C": GREEN, # No specific critique found for G.
        "Reviewer D": GREEN, # Listed as Correct for G.
        "Reviewer G": GREEN, # Self-review lists as Correct for G.
        "Reviewer O": GREEN, # Listed as Accurate for G.
        "Reviewer Q": GREEN, # Listed as Accurate for G.
    },
}

# --- 7. Closed category ---
# Defined by AgentO, AgentQ, AgentC, AgentG. AgentD does not appear to define it in provided sources.
results["Closed category"] = {
    "AgentD": {
        "Reviewer C": N_A,
        "Reviewer D": N_A,
        "Reviewer G": N_A,
        "Reviewer O": N_A,
        "Reviewer Q": N_A,
    },
    "AgentO": {
        "Reviewer C": GREEN, # No specific critique found for O.
        "Reviewer D": GREEN, # Listed as Correct for O.
        "Reviewer G": GREEN, # Listed as Accurate for O.
        "Reviewer O": GREEN, # No specific critique found.
        "Reviewer Q": GREEN, # No specific critique found for O.
    },
    "AgentQ": {
        "Reviewer C": GREEN, # No specific critique found for Q.
        "Reviewer D": GREEN, # No specific critique found for Q.
        "Reviewer G": GREEN, # No specific critique found for Q.
        "Reviewer O": ORANGE, # "Standard usage is monoidal closed. The draft divorces the internal-hom from a tensor." for Q.
        "Reviewer Q": GREEN, # Self-review lists as Correct for Q.
    },
    "AgentC": {
        "Reviewer C": GREEN, # No self-critique found for C.
        "Reviewer D": GREEN, # No specific critique found for C.
        "Reviewer G": GREEN, # Listed as Accurate for C.
        "Reviewer O": GREEN, # No specific critique found for C.
        "Reviewer Q": GREEN, # No specific critique found for C.
    },
    "AgentG": {
        "Reviewer C": GREEN, # No specific critique found for G.
        "Reviewer D": GREEN, # No specific critique found for G.
        "Reviewer G": ORANGE, # "Mostly Accurate. It should be specified that this is a category enriched over itself." for G.
        "Reviewer O": GREEN, # Listed as Accurate for G.
        "Reviewer Q": GREEN, # No specific critique found for G.
    },
}

# --- 8. Coefficient ---
# Defined by AgentD, AgentO, AgentQ, AgentC, AgentG
results["Coefficient"] = {
    "AgentD": {
        "Reviewer C": GREEN, # No specific critique found for DS.
        "Reviewer D": GREEN, # No specific critique found for DS.
        "Reviewer G": ORANGE, # "Definition too vague and context-dependent" for DS.
        "Reviewer O": ORANGE, # "Definition is too vague and context‐dependent." for DS.
        "Reviewer Q": GREEN, # No specific critique found for DS.
    },
    "AgentO": {
        "Reviewer C": ORANGE, # "This definition is too vague." for O.
        "Reviewer D": GREEN, # "Acceptable (vague but contextually fine)." for O.
        "Reviewer G": GREEN, # "A good, if informal, description." for O.
        "Reviewer O": GREEN, # No specific critique found.
        "Reviewer Q": ORANGE, # "Too vague. ... should be more precise." for O.
    },
    "AgentQ": {
        "Reviewer C": GREEN, # No specific critique found for Q.
        "Reviewer D": ORANGE, # "Vague. In enriched categories, a 'coefficient' is an object in the base monoidal category" for Q.
        "Reviewer G": ORANGE, # "Ambiguous. In enriched category theory, "coefficient" isn't standard terminology." for Q.
        "Reviewer O": ORANGE, # "Too vague to count as a definition." for Q.
        "Reviewer Q": ORANGE, # "Slightly vague but acceptable in context." for Q.
    },
    "AgentC": {
        "Reviewer C": GREEN, # No self-critique found for C.
        "Reviewer D": RED, # "Misleading. *Correction*: In enriched category theory, the **enriching category** $\mathcal{V}$ is the "base," not "coefficients."" for C.
        "Reviewer G": GREEN, # Listed as Accurate for C.
        "Reviewer O": ORANGE, # "Not standard terminology in enriched category theory." for C.
        "Reviewer Q": GREEN, # No specific critique found for C.
    },
    "AgentG": {
        "Reviewer C": ORANGE, # "could be expanded slightly to clarify Lawvere's specific usage" for G.
        "Reviewer D": ORANGE, # "Ambiguous – ... could be more precise." for G.
        "Reviewer G": GREEN, # Self-review lists as Accurate for G.
        "Reviewer O": ORANGE, # "This term as stated is not standard" for G.
        "Reviewer Q": ORANGE, # "Ambiguous." for G.
    },
}

# --- 9. Cosegment ---
# Defined by AgentD, AgentO, AgentQ, AgentC, AgentG
results["Cosegment"] = {
    "AgentD": {
        "Reviewer C": GREEN, # No specific critique found for DS.
        "Reviewer D": GREEN, # No specific critique found for DS.
        "Reviewer G": GREEN, # Listed as Accurate for DS.
        "Reviewer O": ORANGE, # "“Morphism from an initial object (dual to segment)” is not standard terminology." for DS.
        "Reviewer Q": GREEN, # No specific critique found for DS.
    },
    "AgentO": {
        "Reviewer C": ORANGE, # "The definition given ("initial object together with two coproduct injections 0→1⊔1") is non-standard." for O.
        "Reviewer D": RED, # "Incorrect. Not standard; likely confusion with bipointed categories or zero objects. Omit or redefine." for O.
        "Reviewer G": ORANGE, # "Minor Correction. The definition is slightly off. ... cosegment object is the pushout of the codiagonal" for O.
        "Reviewer O": ORANGE, # "The provided definition is non-standard and likely incorrect." for O (from overall summary).
        "Reviewer Q": ORANGE, # "Unclear: This term is not commonly used or well-established. It may refer to a specific construction in some contexts but lacks clarity here." for O.
    },
    "AgentQ": {
        "Reviewer C": ORANGE, # "The given definition appears to conflate this with concepts from model categories." for Q.
        "Reviewer D": ORANGE, # "Inaccurate. The term "cosegment" is non-standard. The definition describes a path object" for Q.
        "Reviewer G": GREEN, # "Accurate. This is a correct, though specialized, definition used in contexts like model categories to define interval objects." for Q.
        "Reviewer O": ORANGE, # "Definition given is model–category-specific and not a standard categorical notion; readers might infer it is universally accepted." for Q.
        "Reviewer Q": ORANGE, # "The definition is non-standard and seems to describe a path object in a model category. It should be clarified or labeled as non-standard." for Q.
    },
    "AgentC": {
        "Reviewer C": GREEN, # No self-critique found for C.
        "Reviewer D": RED, # "Non-standard term. *Correction*: Typically called a **cospan** or **interval object**." for C.
        "Reviewer G": ORANGE, # "Less standard than 'object with two global elements'" for C.
        "Reviewer O": GREEN, # "An uncommon term, but your description 'two maps from the terminal object' is exactly the dual of a segment." for C.
        "Reviewer Q": GREEN, # No specific critique found for C.
    },
    "AgentG": {
        "Reviewer C": ORANGE, # "The definition is noted as 'less common' but could benefit from a more precise statement, as it appears in Reedy category theory" for G.
        "Reviewer D": ORANGE, # "Problematic – 'Cosegment' is non-standard." for G.
        "Reviewer G": GREEN, # Self-review lists as Accurate for G.
        "Reviewer O": ORANGE, # "This term as stated is not standard" for G.
        "Reviewer Q": ORANGE, # "Too vague / Not commonly used." for G.
    },
}

# --- 10. Day Convolution ---
# Defined by AgentD, AgentO, AgentC, AgentG. AgentQ is not explicitly mentioned as defining it.
results["Day Convolution"] = {
    "AgentD": {
        "Reviewer C": GREEN, # No specific critique found for DS.
        "Reviewer D": GREEN, # No specific critique found for DS.
        "Reviewer G": GREEN, # Listed as Accurate for DS.
        "Reviewer O": GREEN, # No specific critique found for DS.
        "Reviewer Q": GREEN, # No specific critique found for DS.
    },
    "AgentO": {
        "Reviewer C": GREEN, # No specific critique found for O.
        "Reviewer D": GREEN, # Listed as Correct for O.
        "Reviewer G": RED, # "Correction. The formula is incorrect. ... describes the internal hom" for O.
        "Reviewer O": RED, # "The formula provided was for the internal hom, not the Day convolution tensor product" for O (from overall summary).
        "Reviewer Q": GREEN, # No specific critique found for O.
    },
    "AgentQ": {
        "Reviewer C": N_A,
        "Reviewer D": N_A,
        "Reviewer G": N_A,
        "Reviewer O": N_A,
        "Reviewer Q": N_A,
    },
    "AgentC": {
        "Reviewer C": GREEN, # No self-critique found for C.
        "Reviewer D": GREEN, # Listed as Correct for C.
        "Reviewer G": RED, # "Issue: Formula is ill-formed as written" for C.
        "Reviewer O": GREEN, # No specific critique found for C.
        "Reviewer Q": GREEN, # No specific critique found for C.
    },
    "AgentG": {
        "Reviewer C": GREEN, # No specific critique found for G.
        "Reviewer D": GREEN, # No specific critique found for G.
        "Reviewer G": GREEN, # Self-review lists as Accurate for G.
        "Reviewer O": GREEN, # No specific critique found for G.
        "Reviewer Q": GREEN, # No specific critique found for G.
    },
}

# --- 11. Dinatural Transformation ---
# Defined by AgentD, AgentQ, AgentC, AgentG. AgentO is not explicitly mentioned as defining it.
results["Dinatural Transformation"] = {
    "AgentD": {
        "Reviewer C": GREEN, # No specific critique found for DS.
        "Reviewer D": GREEN, # No specific critique found for DS.
        "Reviewer G": GREEN, # Listed as Accurate for DS.
        "Reviewer O": GREEN, # No specific critique found for DS.
        "Reviewer Q": GREEN, # No specific critique found for DS.
    },
    "AgentO": {
        "Reviewer C": N_A,
        "Reviewer D": N_A,
        "Reviewer G": N_A,
        "Reviewer O": N_A,
        "Reviewer Q": N_A,
    },
    "AgentQ": {
        "Reviewer C": GREEN, # No specific critique found for Q.
        "Reviewer D": ORANGE, # "Incomplete. Must specify the hexagon condition" for Q.
        "Reviewer G": ORANGE, # "The definition is too vague. A diagram is needed to show the coherence condition." for Q.
        "Reviewer O": ORANGE, # "Only says "satisfies a coherence condition"." for Q.
        "Reviewer Q": GREEN, # Self-review lists as Correct for Q.
    },
    "AgentC": {
        "Reviewer C": GREEN, # No self-critique found for C.
        "Reviewer D": GREEN, # Listed as Correct for C.
        "Reviewer G": GREEN, # Listed as Accurate for C.
        "Reviewer O": GREEN, # Listed as Correct for C.
        "Reviewer Q": GREEN, # No specific critique found for C.
    },
    "AgentG": {
        "Reviewer C": GREEN, # No specific critique found for G.
        "Reviewer D": GREEN, # Listed as Correct for G.
        "Reviewer G": GREEN, # Self-review lists as Correct for G.
        "Reviewer O": GREEN, # Listed as Accurate for G.
        "Reviewer Q": GREEN, # No specific critique found for G.
    },
}

# --- 12. Exact category ---
# Defined by AgentD, AgentO, AgentQ, AgentC, AgentG
results["Exact category"] = {
    "AgentD": {
        "Reviewer C": GREEN, # No specific critique found for DS.
        "Reviewer D": GREEN, # No specific critique found for DS.
        "Reviewer G": RED, # "Incorrect. This definition is confused with something else. The "Eilenberg–Moore axioms" refer to monads." for DS.
        "Reviewer O": RED, # "“Eilenberg–Moore axioms" is not the usual reference for Quillen's exact categories." for DS.
        "Reviewer Q": GREEN, # Self-review says "Refers to Eilenberg–Moore axioms; acceptable" for DS.
    },
    "AgentO": {
        "Reviewer C": GREEN, # No specific critique found for O.
        "Reviewer D": GREEN, # Listed as Correct for O.
        "Reviewer G": GREEN, # Listed as Accurate for O.
        "Reviewer O": GREEN, # No specific critique found.
        "Reviewer Q": GREEN, # Listed as Accurate for O.
    },
    "AgentQ": {
        "Reviewer C": GREEN, # No specific critique found for Q.
        "Reviewer D": GREEN, # Listed as Correct for Q.
        "Reviewer G": GREEN, # No specific critique found for Q.
        "Reviewer O": GREEN, # Listed as Correct for Q.
        "Reviewer Q": GREEN, # Self-review lists as Correct for Q.
    },
    "AgentC": {
        "Reviewer C": GREEN, # No self-critique found for C.
        "Reviewer D": GREEN, # Listed as Correct for C.
        "Reviewer G": GREEN, # Listed as Accurate for C.
        "Reviewer O": GREEN, # "You have the right idea: an additive category plus a Quillen‐style class of 'short exact sequences.'" for C.
        "Reviewer Q": GREEN, # No specific critique found for C.
    },
    "AgentG": {
        "Reviewer C": GREEN, # No specific critique found for G.
        "Reviewer D": GREEN, # Listed as Correct for G.
        "Reviewer G": GREEN, # Self-review lists as Correct for G.
        "Reviewer O": GREEN, # Listed as Accurate for G.
        "Reviewer Q": GREEN, # Listed as Correct for G.
    },
}

# --- 13. Factorization System ---
# Defined by AgentD, AgentO, AgentQ, AgentC, AgentG
results["Factorization System"] = {
    "AgentD": {
        "Reviewer C": GREEN, # No specific critique found for DS.
        "Reviewer D": GREEN, # No specific critique found for DS.
        "Reviewer G": GREEN, # Listed as Accurate for DS.
        "Reviewer O": GREEN, # No specific critique found for DS.
        "Reviewer Q": GREEN, # No specific critique found for DS.
    },
    "AgentO": {
        "Reviewer C": GREEN, # No specific critique found for O.
        "Reviewer D": GREEN, # Listed as Correct for O.
        "Reviewer G": ORANGE, # "Minor Correction. The orthogonality condition is usually stated as: for any commutative square... there exists a *unique* diagonal filler." for O.
        "Reviewer O": ORANGE, # "The definition for 1-categories should explicitly mention the *uniqueness* of the diagonal filler, which was omitted." for O.
        "Reviewer Q": GREEN, # Listed as Accurate for O.
    },
    "AgentQ": {
        "Reviewer C": GREEN, # No specific critique found for Q.
        "Reviewer D": GREEN, # Listed as Correct for Q.
        "Reviewer G": ORANGE, # "The term "orthogonal" should be defined explicitly by stating the **unique lifting property**." for Q.
        "Reviewer O": ORANGE, # "Orthogonal" is mentioned but the *unique lifting property* is what orthogonality means." for Q.
        "Reviewer Q": GREEN, # Self-review lists as Correct for Q.
    },
    "AgentC": {
        "Reviewer C": GREEN, # No self-critique found for C.
        "Reviewer D": GREEN, # Listed as Correct for C.
        "Reviewer G": GREEN, # Listed as Accurate for C.
        "Reviewer O": GREEN, # Listed as Correct for C.
        "Reviewer Q": GREEN, # No specific critique found for C.
    },
    "AgentG": {
        "Reviewer C": GREEN, # No specific critique found for G.
        "Reviewer D": GREEN, # Listed as Correct for G.
        "Reviewer G": GREEN, # Self-review lists as Accurate for G.
        "Reviewer O": GREEN, # Listed as Accurate for G.
        "Reviewer Q": ORANGE, # "Uniqueness condition needs clarification" for G.
    },
}

# --- 14. Flexible Limit ---
# Defined by AgentO, AgentQ, AgentC, AgentG. AgentD does not appear to define it in provided sources.
results["Flexible Limit"] = {
    "AgentD": {
        "Reviewer C": N_A,
        "Reviewer D": N_A,
        "Reviewer G": N_A,
        "Reviewer O": N_A,
        "Reviewer Q": N_A,
    },
    "AgentO": {
        "Reviewer C": GREEN, # No specific critique found for O.
        "Reviewer D": GREEN, # Listed as Correct for O.
        "Reviewer G": GREEN, # Listed as Accurate for O.
        "Reviewer O": GREEN, # No specific critique found.
        "Reviewer Q": GREEN, # No specific critique found for O.
    },
    "AgentQ": {
        "Reviewer C": GREEN, # No specific critique found for Q.
        "Reviewer D": RED, # "Inaccurate. A flexible limit is a type of 2-dimensional limit that is better described as a cofibrant replacement of a strict 2-limit" for Q.
        "Reviewer G": GREEN, # No specific critique found for Q.
        "Reviewer O": GREEN, # No specific critique found for Q.
        "Reviewer Q": GREEN, # Self-review says `flexible limit` is correct for Q.
    },
    "AgentC": {
        "Reviewer C": GREEN, # No self-critique found for C.
        "Reviewer D": GREEN, # Listed as Correct for C.
        "Reviewer G": GREEN, # Listed as Accurate for C.
        "Reviewer O": GREEN, # No specific critique found for C.
        "Reviewer Q": GREEN, # No specific critique found for C.
    },
    "AgentG": {
        "Reviewer C": GREEN, # No specific critique found for G.
        "Reviewer D": GREEN, # Listed as Correct for G.
        "Reviewer G": GREEN, # Self-review lists as Accurate for G.
        "Reviewer O": GREEN, # No specific critique found for G.
        "Reviewer Q": GREEN, # No specific critique found for G.
    },
}

# --- 15. Geometric Langlands Program ---
# Defined by AgentD, AgentO, AgentQ, AgentC, AgentG
results["Geometric Langlands Program"] = {
    "AgentD": {
        "Reviewer C": YELLOW, # "Non-standard notation for Langlands dual group." for DS.
        "Reviewer D": GREEN, # No specific critique found for DS.
        "Reviewer G": GREEN, # No specific critique found for DS.
        "Reviewer O": GREEN, # No specific critique found for DS.
        "Reviewer Q": GREEN, # No specific critique found for DS.
    },
    "AgentO": {
        "Reviewer C": GREEN, # No specific critique found for O.
        "Reviewer D": GREEN, # Listed as Correct for O.
        "Reviewer G": GREEN, # Listed as Accurate for O.
        "Reviewer O": GREEN, # No specific critique found.
        "Reviewer Q": GREEN, # Listed as Accurate for O.
    },
    "AgentQ": {
        "Reviewer C": GREEN, # No specific critique found for Q.
        "Reviewer D": GREEN, # Listed as Correct for Q.
        "Reviewer G": GREEN, # Listed as Accurate for Q.
        "Reviewer O": GREEN, # No specific critique found for Q.
        "Reviewer Q": GREEN, # Self-review lists as Correct for Q.
    },
    "AgentC": {
        "Reviewer C": GREEN, # No self-critique found for C.
        "Reviewer D": GREEN, # Listed as Correct for C.
        "Reviewer G": GREEN, # Listed as Accurate for C.
        "Reviewer O": GREEN, # No specific critique found for C.
        "Reviewer Q": GREEN, # No specific critique found for C.
    },
    "AgentG": {
        "Reviewer C": GREEN, # No specific critique found for G.
        "Reviewer D": GREEN, # Listed as Correct for G.
        "Reviewer G": GREEN, # Self-review lists as Accurate for G.
        "Reviewer O": GREEN, # Listed as Accurate for G.
        "Reviewer Q": GREEN, # No specific critique found for G.
    },
}

# --- 16. Globular set ---
# Defined by AgentD, AgentO, AgentQ, AgentC, AgentG (AgentC defines "Globular k-cell" as a related but distinct term)
results["Globular set"] = {
    "AgentD": {
        "Reviewer C": RED, # "The definition mentions morphisms s,t: n -> n+1, but this should be s,t: n+1 -> n (source and target go from higher to lower dimensions)." for DS.
        "Reviewer D": GREEN, # No specific critique found for DS.
        "Reviewer G": GREEN, # No specific critique found for DS.
        "Reviewer O": GREEN, # No specific critique found for DS.
        "Reviewer Q": GREEN, # No specific critique found for DS.
    },
    "AgentO": {
        "Reviewer C": GREEN, # No specific critique found for O.
        "Reviewer D": GREEN, # Listed as Correct for O.
        "Reviewer G": GREEN, # No specific critique found for O.
        "Reviewer O": GREEN, # No specific critique found.
        "Reviewer Q": GREEN, # No specific critique found for O.
    },
    "AgentQ": {
        "Reviewer C": GREEN, # No specific critique found for Q.
        "Reviewer D": GREEN, # Listed as Correct for Q.
        "Reviewer G": GREEN, # No specific critique found for Q.
        "Reviewer O": GREEN, # No specific critique found for Q.
        "Reviewer Q": GREEN, # Self-review lists as Correct for Q.
    },
    "AgentC": { # For "Globular k-cell" (AgentC's actual term defined)
        "Reviewer C": GREEN, # No self-critique found for C.
        "Reviewer D": GREEN, # Listed as Correct for C.
        "Reviewer G": GREEN, # Listed as Accurate for C.
        "Reviewer O": GREEN, # No specific critique found for C.
        "Reviewer Q": GREEN, # No specific critique found for C.
    },
    "AgentG": {
        "Reviewer C": GREEN, # No specific critique found for G.
        "Reviewer D": GREEN, # Listed as Correct for G.
        "Reviewer G": GREEN, # Self-review lists as Accurate for G.
        "Reviewer O": GREEN, # No specific critique found for G.
        "Reviewer Q": GREEN, # No specific critique found for G.
    },
}

# --- 17. Grothendieck Duality ---
# Defined by AgentD, AgentO, AgentQ, AgentC, AgentG
results["Grothendieck Duality"] = {
    "AgentD": {
        "Reviewer C": GREEN, # No specific critique found for DS.
        "Reviewer D": GREEN, # No specific critique found for DS.
        "Reviewer G": GREEN, # No specific critique found for DS.
        "Reviewer O": GREEN, # No specific critique found for DS.
        "Reviewer Q": GREEN, # No specific critique found for DS.
    },
    "AgentO": {
        "Reviewer C": GREEN, # No specific critique found for O.
        "Reviewer D": GREEN, # Listed as Correct for O.
        "Reviewer G": GREEN, # Listed as Accurate for O.
        "Reviewer O": GREEN, # No specific critique found.
        "Reviewer Q": GREEN, # Listed as Accurate for O.
    },
    "AgentQ": {
        "Reviewer C": GREEN, # No specific critique found for Q.
        "Reviewer D": GREEN, # No specific critique found for Q.
        "Reviewer G": GREEN, # No specific critique found for Q.
        "Reviewer O": GREEN, # No specific critique found for Q.
        "Reviewer Q": GREEN, # No specific critique found for Q.
    },
    "AgentC": {
        "Reviewer C": GREEN, # No self-critique found for C.
        "Reviewer D": ORANGE, # "Incomplete. *Correction*: General form is... (not just G = O_Y)" for C.
        "Reviewer G": ORANGE, # "Issue: Formula given is an instance rather than the definition" for C.
        "Reviewer O": GREEN, # No specific critique found for C.
        "Reviewer Q": GREEN, # No specific critique found for C.
    },
    "AgentG": {
        "Reviewer C": GREEN, # No specific critique found for G.
        "Reviewer D": GREEN, # Listed as Correct for G.
        "Reviewer G": GREEN, # Self-review lists as Accurate for G.
        "Reviewer O": GREEN, # Listed as Accurate for G.
        "Reviewer Q": GREEN, # No specific critique found for G.
    },
}

# --- 18. Grothendieck fibration ---
# Defined by AgentD, AgentO, AgentQ, AgentC, AgentG
results["Grothendieck fibration"] = {
    "AgentD": {
        "Reviewer C": ORANGE, # "The definition is informal ("cartesianly") but essentially correct." for DS.
        "Reviewer D": GREEN, # No specific critique found for DS.
        "Reviewer G": GREEN, # Listed as Accurate for DS.
        "Reviewer O": ORANGE, # "The description "morphisms in E lift 'cartesianly'" is shorthand." for DS.
        "Reviewer Q": GREEN, # No specific critique found for DS.
    },
    "AgentO": {
        "Reviewer C": GREEN, # No specific critique found for O.
        "Reviewer D": GREEN, # Listed as Correct for O.
        "Reviewer G": GREEN, # Listed as Accurate for O.
        "Reviewer O": GREEN, # No specific critique found.
        "Reviewer Q": GREEN, # Listed as Accurate for O.
    },
    "AgentQ": {
        "Reviewer C": GREEN, # No specific critique found for Q.
        "Reviewer D": GREEN, # Listed as Correct for Q.
        "Reviewer G": GREEN, # Listed as Accurate for Q.
        "Reviewer O": ORANGE, # "Needs the *chosen lift* to be **cartesian** and stable under composition." for Q.
        "Reviewer Q": GREEN, # Self-review lists as Correct for Q.
    },
    "AgentC": {
        "Reviewer C": GREEN, # No self-critique found for C.
        "Reviewer D": GREEN, # Listed as Correct for C.
        "Reviewer G": GREEN, # Listed as Accurate for C.
        "Reviewer O": GREEN, # "Correct (one usually unpacks 'cartesian lifting' further, but you've given the heart of it)." for C.
        "Reviewer Q": GREEN, # Listed as Correct for C.
    },
    "AgentG": {
        "Reviewer C": GREEN, # No specific critique found for G.
        "Reviewer D": GREEN, # Listed as Correct for G.
        "Reviewer G": GREEN, # Self-review lists as Accurate for G.
        "Reviewer O": GREEN, # Listed as Accurate for G.
        "Reviewer Q": GREEN, # No specific critique found for G.
    },
}

# --- 19. Hochschild cohomology ---
# Defined by AgentD, AgentO, AgentQ, AgentC, AgentG
results["Hochschild cohomology"] = {
    "AgentD": {
        "Reviewer C": YELLOW, # "Typographical error in the mathematical formula." for DS.
        "Reviewer D": GREEN, # No specific critique found for DS.
        "Reviewer G": YELLOW, # "Typographical error in the mathematical formula." for DS.
        "Reviewer O": GREEN, # No specific critique found for DS.
        "Reviewer Q": GREEN, # No specific critique found for DS.
    },
    "AgentO": {
        "Reviewer C": GREEN, # No specific critique found for O.
        "Reviewer D": GREEN, # Listed as Correct for O.
        "Reviewer G": GREEN, # Listed as Accurate for O.
        "Reviewer O": GREEN, # No specific critique found.
        "Reviewer Q": GREEN, # Listed as Accurate for O.
    },
    "AgentQ": {
        "Reviewer C": GREEN, # No specific critique found for Q.
        "Reviewer D": GREEN, # Listed as Correct for Q.
        "Reviewer G": GREEN, # Listed as Accurate for Q.
        "Reviewer O": GREEN, # No specific critique found for Q.
        "Reviewer Q": GREEN, # Self-review lists as Correct for Q.
    },
    "AgentC": {
        "Reviewer C": GREEN, # No self-critique found for C.
        "Reviewer D": GREEN, # Listed as Correct for C.
        "Reviewer G": GREEN, # Listed as Accurate for C.
        "Reviewer O": GREEN, # No specific critique found for C.
        "Reviewer Q": GREEN, # No specific critique found for C.
    },
    "AgentG": {
        "Reviewer C": GREEN, # No specific critique found for G.
        "Reviewer D": GREEN, # Listed as Correct for G.
        "Reviewer G": ORANGE, # "Mostly Accurate. The notation is slightly off." for G (self-critique).
        "Reviewer O": GREEN, # Listed as Accurate for G.
        "Reviewer Q": GREEN, # No specific critique found for G.
    },
}

# --- 20. Homotopy Coherent Diagram ---
# Defined by AgentD, AgentO, AgentQ, AgentC, AgentG
results["Homotopy Coherent Diagram"] = {
    "AgentD": {
        "Reviewer C": GREEN, # No specific critique found for DS.
        "Reviewer D": GREEN, # No specific critique found for DS.
        "Reviewer G": GREEN, # Listed as Accurate for DS.
        "Reviewer O": GREEN, # No specific critique found for DS.
        "Reviewer Q": GREEN, # No specific critique found for DS.
    },
    "AgentO": {
        "Reviewer C": GREEN, # No specific critique found for O.
        "Reviewer D": GREEN, # Listed as Correct for O.
        "Reviewer G": GREEN, # Listed as Accurate for O.
        "Reviewer O": GREEN, # No specific critique found.
        "Reviewer Q": GREEN, # Listed as Accurate for O.
    },
    "AgentQ": {
        "Reviewer C": ORANGE, # "The definition could be clearer. It can be defined more precisely as a functor of ∞-categories..." for Q.
        "Reviewer D": GREEN, # Listed as Correct for Q.
        "Reviewer G": GREEN, # No specific critique found for Q.
        "Reviewer O": GREEN, # No specific critique found for Q.
        "Reviewer Q": GREEN, # Self-review lists as Correct for Q.
    },
    "AgentC": {
        "Reviewer C": GREEN, # No self-critique found for C.
        "Reviewer D": GREEN, # No specific critique found for C.
        "Reviewer G": GREEN, # Listed as Accurate for C.
        "Reviewer O": GREEN, # No specific critique found for C.
        "Reviewer Q": GREEN, # No specific critique found for C.
    },
    "AgentG": {
        "Reviewer C": GREEN, # No specific critique found for G.
        "Reviewer D": GREEN, # Listed as Correct for G.
        "Reviewer G": GREEN, # Self-review lists as Accurate for G.
        "Reviewer O": GREEN, # Listed as Accurate for G.
        "Reviewer Q": GREEN, # No specific critique found for G.
    },
}

# --- 21. Icon ---
# Defined by AgentD, AgentO, AgentQ, AgentC, AgentG
results["Icon"] = {
    "AgentD": {
        "Reviewer C": GREEN, # No specific critique found for DS.
        "Reviewer D": GREEN, # No specific critique found for DS.
        "Reviewer G": GREEN, # Listed as Accurate for DS.
        "Reviewer O": GREEN, # No specific critique found for DS.
        "Reviewer Q": GREEN, # No specific critique found for DS.
    },
    "AgentO": {
        "Reviewer C": GREEN, # No specific critique found for O.
        "Reviewer D": GREEN, # Listed as Correct for O.
        "Reviewer G": GREEN, # Listed as Accurate for O.
        "Reviewer O": GREEN, # No specific critique found.
        "Reviewer Q": GREEN, # Listed as Accurate for O.
    },
    "AgentQ": {
        "Reviewer C": ORANGE, # "While the definition captures the idea, it should specify that an **icon** is an identity-on-objects, identity-on-1-cells lax natural transformation between lax functors." for Q.
        "Reviewer D": GREEN, # Listed as Correct for Q.
        "Reviewer G": GREEN, # No specific critique found for Q.
        "Reviewer O": GREEN, # Listed as Correct for Q.
        "Reviewer Q": GREEN, # Self-review lists as Correct for Q.
    },
    "AgentC": {
        "Reviewer C": GREEN, # No self-critique found for C.
        "Reviewer D": RED, # "Incorrect. An **icon** is a lax natural transformation with identity 1-cell components (for bicategories), not a 2-morphism in a double category." for C.
        "Reviewer G": GREEN, # Listed as Accurate for C.
        "Reviewer O": GREEN, # No specific critique found for C.
        "Reviewer Q": GREEN, # No specific critique found for C.
    },
    "AgentG": {
        "Reviewer C": GREEN, # No specific critique found for G.
        "Reviewer D": GREEN, # No specific critique found for G.
        "Reviewer G": GREEN, # Self-review lists as Accurate for G.
        "Reviewer O": GREEN, # Listed as Accurate for G.
        "Reviewer Q": GREEN, # No specific critique found for G.
    },
}

# --- 22. Image ---
# Defined by AgentD, AgentO, AgentQ, AgentC, AgentG
results["Image"] = {
    "AgentD": {
        "Reviewer C": GREEN, # No specific critique found for DS.
        "Reviewer D": GREEN, # No specific critique found for DS.
        "Reviewer G": GREEN, # Listed as Accurate for DS.
        "Reviewer O": GREEN, # No specific critique found for DS.
        "Reviewer Q": GREEN, # No specific critique found for DS.
    },
    "AgentO": {
        "Reviewer C": GREEN, # No specific critique found for O.
        "Reviewer D": GREEN, # Listed as Correct for O.
        "Reviewer G": GREEN, # Listed as Accurate for O.
        "Reviewer O": GREEN, # No specific critique found.
        "Reviewer Q": GREEN, # Listed as Accurate for O.
    },
    "AgentQ": {
        "Reviewer C": GREEN, # No specific critique found for Q.
        "Reviewer D": GREEN, # Listed as Correct for Q.
        "Reviewer G": ORANGE, # "Clarification Recommended. The definition conflates the general notion of an image with a specific construction (the regular image)." for Q.
        "Reviewer O": GREEN, # No specific critique found for Q.
        "Reviewer Q": GREEN, # Self-review lists as Correct for Q.
    },
    "AgentC": {
        "Reviewer C": GREEN, # No self-critique found for C.
        "Reviewer D": ORANGE, # "Context-dependent. Requires a regular category (where images exist)." for C.
        "Reviewer G": GREEN, # Listed as Accurate for C.
        "Reviewer O": GREEN, # Listed as Correct for C.
        "Reviewer Q": GREEN, # Listed as Correct for C.
    },
    "AgentG": {
        "Reviewer C": GREEN, # No specific critique found for G.
        "Reviewer D": RED, # "Inaccurate for regular image – The regular image of (f: X \to Y) is the coequalizer of its kernel pair, not "the equalizer of the cokernel pair"." for G.
        "Reviewer G": GREEN, # Self-review lists as Accurate for G.
        "Reviewer O": RED, # "The **categorical (or regular) image** of f is the **kernel of its cokernel**. ... You have these two constructions swapped." for G.
        "Reviewer Q": ORANGE, # "Mostly correct. ... The regular image via coequalizer of kernel pair is better for general categories." for G.
    },
}

# --- 23. Locally Presentable Category ---
# Defined by AgentD, AgentO, AgentQ, AgentC, AgentG
results["Locally Presentable Category"] = {
    "AgentD": {
        "Reviewer C": GREEN, # No specific critique found for DS.
        "Reviewer D": GREEN, # No specific critique found for DS.
        "Reviewer G": GREEN, # Listed as Accurate for DS.
        "Reviewer O": GREEN, # No specific critique found for DS.
        "Reviewer Q": GREEN, # No specific critique found for DS.
    },
    "AgentO": {
        "Reviewer C": GREEN, # No specific critique found for O.
        "Reviewer D": GREEN, # Listed as Correct for O.
        "Reviewer G": GREEN, # Listed as Accurate for O.
        "Reviewer O": GREEN, # No specific critique found.
        "Reviewer Q": GREEN, # Listed as Accurate for O.
    },
    "AgentQ": {
        "Reviewer C": ORANGE, # "The definition should be more precise: A **locally presentable category** is a cocomplete category that has a small set of κ-compact generators for some regular cardinal κ." for Q.
        "Reviewer D": ORANGE, # "Imprecise. Must specify **accessibility** + cocompleteness" for Q.
        "Reviewer G": GREEN, # No specific critique found for Q.
        "Reviewer O": ORANGE, # "Must involve a regular cardinal λ." for Q.
        "Reviewer Q": GREEN, # Self-review lists as Correct for Q.
    },
    "AgentC": {
        "Reviewer C": GREEN, # No self-critique found for C.
        "Reviewer D": GREEN, # Listed as Correct for C.
        "Reviewer G": RED, # "Missing: The generating set must be explicitly stated as a 'small set'" for C.
        "Reviewer O": GREEN, # "You need 'cocomplete + accessible...'. That's exactly what you said." for C.
        "Reviewer Q": GREEN, # No specific critique found for C.
    },
    "AgentG": {
        "Reviewer C": GREEN, # No specific critique found for G.
        "Reviewer D": GREEN, # Listed as Correct for G.
        "Reviewer G": GREEN, # Self-review lists as Accurate for G.
        "Reviewer O": GREEN, # Listed as Accurate for G.
        "Reviewer Q": GREEN, # No specific critique found for G.
    },
}

# --- 24. Monoidal ∞-category ---
# Defined by AgentD, AgentO, AgentQ, AgentC, AgentG
results["Monoidal ∞-category"] = {
    "AgentD": {
        "Reviewer C": GREEN, # No specific critique found for DS.
        "Reviewer D": GREEN, # No specific critique found for DS.
        "Reviewer G": GREEN, # Listed as Accurate for DS.
        "Reviewer O": GREEN, # No specific critique found for DS.
        "Reviewer Q": GREEN, # No specific critique found for DS.
    },
    "AgentO": {
        "Reviewer C": GREEN, # No specific critique found for O.
        "Reviewer D": GREEN, # No specific critique found for O.
        "Reviewer G": GREEN, # Listed as Accurate for O.
        "Reviewer O": RED, # "The definition incorrectly identifies the target operad as N(Γ), which is for *commutative* monoids. ... Correct target should be for associative ($A_\infty$) algebras." for O (from overall summary).
        "Reviewer Q": GREEN, # No specific critique found for O.
    },
    "AgentQ": {
        "Reviewer C": GREEN, # No specific critique found for Q.
        "Reviewer D": GREEN, # No specific critique found for Q.
        "Reviewer G": GREEN, # No specific critique found for Q.
        "Reviewer O": GREEN, # No specific critique found for Q.
        "Reviewer Q": GREEN, # Self-review lists as Correct for Q.
    },
    "AgentC": {
        "Reviewer C": GREEN, # No self-critique found for C.
        "Reviewer D": GREEN, # No specific critique found for C.
        "Reviewer G": RED, # "Incorrect: This is the definition of a **symmetric monoidal** $\infty$-category. The target $N(\mathrm{Fin}_*)$ encodes the symmetric operad. For a general (non-symmetric) monoidal $\infty$-category, the target should be $N(\Delta)$, which corresponds to the associative operad." for C.
        "Reviewer O": GREEN, # No specific critique found for C.
        "Reviewer Q": GREEN, # No specific critique found for C.
    },
    "AgentG": {
        "Reviewer C": GREEN, # No specific critique found for G.
        "Reviewer D": GREEN, # Listed as Correct for G.
        "Reviewer G": GREEN, # Self-review lists as Accurate for G.
        "Reviewer O": GREEN, # Listed as Accurate for G.
        "Reviewer Q": GREEN, # No specific critique found for G.
    },
}

# --- 25. n-category ---
# Defined by AgentO, AgentQ, AgentC, AgentG. AgentD implicitly defines (inf,n)-category.
results["n-category"] = {
    "AgentD": {
        "Reviewer C": N_A,
        "Reviewer D": N_A,
        "Reviewer G": N_A,
        "Reviewer O": N_A,
        "Reviewer Q": N_A,
    },
    "AgentO": {
        "Reviewer C": GREEN, # No specific critique found for O.
        "Reviewer D": GREEN, # Listed as Correct for O.
        "Reviewer G": GREEN, # Listed as Accurate for O.
        "Reviewer O": GREEN, # No specific critique found.
        "Reviewer Q": GREEN, # Listed as Accurate for O.
    },
    "AgentQ": {
        "Reviewer C": GREEN, # No specific critique found for Q.
        "Reviewer D": ORANGE, # "Clarify: Weak (n)-categories have non-strict composition; strict ones are **Set**-enriched for (n=2)." for Q.
        "Reviewer G": GREEN, # No specific critique found for Q.
        "Reviewer O": ORANGE, # "In the weak case the cells above dimension (n) are *invertible*, not identity." for Q.
        "Reviewer Q": GREEN, # Self-review says "Correct" for Q.
    },
    "AgentC": {
        "Reviewer C": GREEN, # No self-critique found for C.
        "Reviewer D": GREEN, # No specific critique found for C.
        "Reviewer G": GREEN, # Listed as Accurate for C.
        "Reviewer O": GREEN, # No specific critique found for C.
        "Reviewer Q": GREEN, # No specific critique found for C.
    },
    "AgentG": {
        "Reviewer C": GREEN, # "The distinction between weak and strict n-categories is properly explained" for G.
        "Reviewer D": GREEN, # Listed as Correct for G.
        "Reviewer G": GREEN, # Self-review lists as Accurate for G.
        "Reviewer O": GREEN, # Listed as Accurate for G.
        "Reviewer Q": GREEN, # No specific critique found for G.
    },
}

# --- 26. Pivotal Category ---
# Defined by AgentO, AgentQ, AgentC, AgentG. AgentD does not define it.
results["Pivotal Category"] = {
    "AgentD": {
        "Reviewer C": N_A,
        "Reviewer D": N_A,
        "Reviewer G": N_A,
        "Reviewer O": N_A,
        "Reviewer Q": N_A,
    },
    "AgentO": {
        "Reviewer C": GREEN, # No specific critique found for O.
        "Reviewer D": GREEN, # Listed as Correct for O.
        "Reviewer G": GREEN, # Listed as Accurate for O.
        "Reviewer O": GREEN, # No specific critique found.
        "Reviewer Q": GREEN, # No specific critique found for O.
    },
    "AgentQ": {
        "Reviewer C": GREEN, # No specific critique found for Q.
        "Reviewer D": GREEN, # Listed as Correct for Q.
        "Reviewer G": GREEN, # No specific critique found for Q.
        "Reviewer O": GREEN, # No specific critique found for Q.
        "Reviewer Q": GREEN, # Self-review lists as Correct for Q.
    },
    "AgentC": {
        "Reviewer C": GREEN, # No self-critique found for C.
        "Reviewer D": GREEN, # No specific critique found for C.
        "Reviewer G": GREEN, # Listed as Accurate for C.
        "Reviewer O": GREEN, # No specific critique found for C.
        "Reviewer Q": GREEN, # No specific critique found for C.
    },
    "AgentG": {
        "Reviewer C": GREEN, # No specific critique found for G.
        "Reviewer D": GREEN, # No specific critique found for G.
        "Reviewer G": ORANGE, # "Mostly Accurate. A pivotal category is a *rigid* monoidal category... The provided definition is a bit too brief." for G.
        "Reviewer O": GREEN, # Listed as Accurate for G.
        "Reviewer Q": GREEN, # No specific critique found for G.
    },
}

# --- 27. Pseudo-algebra ---
# Defined by AgentD, AgentO, AgentQ, AgentC, AgentG
results["Pseudo-algebra"] = {
    "AgentD": {
        "Reviewer C": GREEN, # No specific critique found for DS.
        "Reviewer D": GREEN, # No specific critique found for DS.
        "Reviewer G": RED, # "Pseudo-monad and Pseudo-algebra Definitions - clarity needed" for DS.
        "Reviewer O": GREEN, # No specific critique found for DS.
        "Reviewer Q": GREEN, # No specific critique found for DS.
    },
    "AgentO": {
        "Reviewer C": GREEN, # No specific critique found for O.
        "Reviewer D": GREEN, # No specific critique found for O.
        "Reviewer G": GREEN, # Listed as Accurate for O.
        "Reviewer O": GREEN, # No specific critique found.
        "Reviewer Q": GREEN, # No specific critique found for O.
    },
    "AgentQ": {
        "Reviewer C": GREEN, # No specific critique found for Q.
        "Reviewer D": GREEN, # Listed as Correct for Q.
        "Reviewer G": GREEN, # No specific critique found for Q.
        "Reviewer O": GREEN, # No specific critique found for Q.
        "Reviewer Q": GREEN, # Self-review lists as Correct for Q.
    },
    "AgentC": {
        "Reviewer C": GREEN, # No self-critique found for C.
        "Reviewer D": GREEN, # Listed as Correct for C.
        "Reviewer G": GREEN, # Listed as Accurate for C.
        "Reviewer O": GREEN, # No specific critique found for C.
        "Reviewer Q": GREEN, # No specific critique found for C.
    },
    "AgentG": {
        "Reviewer C": GREEN, # No specific critique found for G.
        "Reviewer D": GREEN, # No specific critique found for G.
        "Reviewer G": GREEN, # Self-review lists as Accurate for G.
        "Reviewer O": GREEN, # Listed as Accurate for G.
        "Reviewer Q": GREEN, # No specific critique found for G.
    },
}

# --- 28. Pseudo-monad ---
# Defined by AgentD, AgentO, AgentQ, AgentC, AgentG
results["Pseudo-monad"] = {
    "AgentD": {
        "Reviewer C": GREEN, # No specific critique found for DS.
        "Reviewer D": GREEN, # No specific critique found for DS.
        "Reviewer G": RED, # "Pseudo-monad and Pseudo-algebra Definitions - clarity needed" for DS.
        "Reviewer O": GREEN, # No specific critique found for DS.
        "Reviewer Q": GREEN, # No specific critique found for DS.
    },
    "AgentO": {
        "Reviewer C": GREEN, # No specific critique found for O.
        "Reviewer D": GREEN, # No specific critique found for O.
        "Reviewer G": GREEN, # Listed as Accurate for O.
        "Reviewer O": GREEN, # No specific critique found.
        "Reviewer Q": GREEN, # No specific critique found for O.
    },
    "AgentQ": {
        "Reviewer C": GREEN, # No specific critique found for Q.
        "Reviewer D": GREEN, # Listed as Correct for Q.
        "Reviewer G": GREEN, # No specific critique found for Q.
        "Reviewer O": GREEN, # No specific critique found for Q.
        "Reviewer Q": GREEN, # Self-review lists as Correct for Q.
    },
    "AgentC": {
        "Reviewer C": GREEN, # No self-critique found for C.
        "Reviewer D": GREEN, # Listed as Correct for C.
        "Reviewer G": GREEN, # Listed as Accurate for C.
        "Reviewer O": GREEN, # No specific critique found for C.
        "Reviewer Q": GREEN, # No specific critique found for C.
    },
    "AgentG": {
        "Reviewer C": GREEN, # No specific critique found for G.
        "Reviewer D": GREEN, # No specific critique found for G.
        "Reviewer G": GREEN, # Self-review lists as Accurate for G.
        "Reviewer O": GREEN, # Listed as Accurate for G.
        "Reviewer Q": GREEN, # No specific critique found for G.
    },
}

# --- 29. Segal Category ---
# Defined by AgentO, AgentQ, AgentG. AgentD, AgentC do not appear to define it in provided sources.
results["Segal Category"] = {
    "AgentD": {
        "Reviewer C": N_A,
        "Reviewer D": N_A,
        "Reviewer G": N_A,
        "Reviewer O": N_A,
        "Reviewer Q": N_A,
    },
    "AgentO": {
        "Reviewer C": GREEN, # No specific critique found for O.
        "Reviewer D": GREEN, # Listed as Correct for O.
        "Reviewer G": GREEN, # Listed as Accurate for O.
        "Reviewer O": RED, # "The definition given... describes a **Segal space**. A Segal category is a simplicial object in **Cat" for O.
        "Reviewer Q": GREEN, # Listed as Accurate for O.
    },
    "AgentQ": {
        "Reviewer C": GREEN, # No specific critique found for Q.
        "Reviewer D": GREEN, # Listed as Correct for Q.
        "Reviewer G": GREEN, # No specific critique found for Q.
        "Reviewer O": GREEN, # Listed as Correct for Q.
        "Reviewer Q": GREEN, # Self-review lists as Correct for Q.
    },
    "AgentC": {
        "Reviewer C": N_A,
        "Reviewer D": N_A,
        "Reviewer G": N_A,
        "Reviewer O": N_A,
        "Reviewer Q": N_A,
    },
    "AgentG": {
        "Reviewer C": GREEN, # No specific critique found for G.
        "Reviewer D": GREEN, # Listed as Correct for G.
        "Reviewer G": GREEN, # Self-review lists as Accurate for G.
        "Reviewer O": GREEN, # Listed as Accurate for G.
        "Reviewer Q": GREEN, # No specific critique found for G.
    },
}

# --- 30. Split Monomorphism / Epimorphism ---
# Defined by AgentD, AgentO, AgentQ, AgentC, AgentG
results["Split Monomorphism / Epimorphism"] = {
    "AgentD": {
        "Reviewer C": GREEN, # No specific critique found for DS.
        "Reviewer D": GREEN, # No specific critique found for DS.
        "Reviewer G": GREEN, # Listed as Accurate for DS.
        "Reviewer O": GREEN, # No specific critique found for DS.
        "Reviewer Q": GREEN, # No specific critique found for DS.
    },
    "AgentO": {
        "Reviewer C": GREEN, # No specific critique found for O.
        "Reviewer D": RED, # "Incorrect; it has a *left* inverse (a retraction), not a right one." for O (from overall summary).
        "Reviewer G": RED, # "Correction. A split mono m has a *right* inverse (a retraction). ... The definition for mono is incorrect; it should be a *left* inverse." for O.
        "Reviewer O": RED, # "The definition for a split monomorphism was incorrect; it has a *left* inverse (a retraction), not a right one." for O.
        "Reviewer Q": GREEN, # No specific critique found for O.
    },
    "AgentQ": {
        "Reviewer C": GREEN, # No specific critique found for Q.
        "Reviewer D": GREEN, # Listed as Correct for Q.
        "Reviewer G": GREEN, # No specific critique found for Q.
        "Reviewer O": GREEN, # No specific critique found for Q.
        "Reviewer Q": GREEN, # Self-review lists as Correct for Q.
    },
    "AgentC": {
        "Reviewer C": GREEN, # No self-critique found for C.
        "Reviewer D": GREEN, # Listed as Correct for C.
        "Reviewer G": GREEN, # Listed as Accurate for C.
        "Reviewer O": GREEN, # Listed as Correct for C.
        "Reviewer Q": GREEN, # Listed as Correct for C.
    },
    "AgentG": {
        "Reviewer C": GREEN, # No specific critique found for G.
        "Reviewer D": GREEN, # Listed as Correct for G.
        "Reviewer G": GREEN, # Self-review lists as Accurate for G.
        "Reviewer O": GREEN, # Listed as Accurate for G.
        "Reviewer Q": GREEN, # No specific critique found for G.
    },
}

# --- 31. Weak Limit / Colimit ---
# Defined by AgentD, AgentO, AgentQ, AgentC, AgentG
results["Weak Limit / Colimit"] = {
    "AgentD": {
        "Reviewer C": GREEN, # No specific critique found for DS.
        "Reviewer D": GREEN, # No specific critique found for DS.
        "Reviewer G": GREEN, # Listed as Accurate for DS.
        "Reviewer O": GREEN, # No specific critique found for DS.
        "Reviewer Q": GREEN, # No specific critique found for DS.
    },
    "AgentO": {
        "Reviewer C": GREEN, # No specific critique found for O.
        "Reviewer D": GREEN, # Listed as Correct (clarification on uniqueness) for O.
        "Reviewer G": RED, # "Correction. Universality is not up to isomorphism, but rather the *existence* of a mediating morphism is guaranteed, but not its *uniqueness*." for O.
        "Reviewer O": ORANGE, # "The definition was imprecise. The universality condition for weak limits guarantees the *existence* of a mediating morphism, but not its uniqueness." for O.
        "Reviewer Q": GREEN, # No specific critique found for O.
    },
    "AgentQ": {
        "Reviewer C": GREEN, # No specific critique found for Q.
        "Reviewer D": GREEN, # Listed as Correct for Q.
        "Reviewer G": GREEN, # No specific critique found for Q.
        "Reviewer O": GREEN, # No specific critique found for Q.
        "Reviewer Q": GREEN, # Self-review lists as Correct for Q.
    },
    "AgentC": {
        "Reviewer C": GREEN, # No self-critique found for C.
        "Reviewer D": GREEN, # Listed as Correct for C.
        "Reviewer G": GREEN, # Listed as Accurate for C.
        "Reviewer O": GREEN, # Listed as Correct for C.
        "Reviewer Q": GREEN, # No specific critique found for C.
    },
    "AgentG": {
        "Reviewer C": GREEN, # No specific critique found for G.
        "Reviewer D": GREEN, # Listed as Correct for G.
        "Reviewer G": GREEN, # Self-review lists as Accurate for G.
        "Reviewer O": GREEN, # Listed as Accurate for G.
        "Reviewer Q": GREEN, # No specific critique found for G.
    },
}

# --- 32. Zero morphism ---
# Defined by AgentD, AgentO, AgentQ, AgentC, AgentG
results["Zero morphism"] = {
    "AgentD": {
        "Reviewer C": GREEN, # No specific critique found for DS.
        "Reviewer D": GREEN, # No specific critique found for DS.
        "Reviewer G": GREEN, # Listed as Accurate for DS.
        "Reviewer O": GREEN, # No specific critique found for DS.
        "Reviewer Q": GREEN, # No specific critique found for DS.
    },
    "AgentO": {
        "Reviewer C": GREEN, # No specific critique found for O.
        "Reviewer D": GREEN, # Listed as Correct for O.
        "Reviewer G": GREEN, # Listed as Accurate for O.
        "Reviewer O": GREEN, # No specific critique found.
        "Reviewer Q": GREEN, # No specific critique found for O.
    },
    "AgentQ": {
        "Reviewer C": GREEN, # No specific critique found for Q.
        "Reviewer D": GREEN, # Listed as Correct for Q.
        "Reviewer G": GREEN, # No specific critique found for Q.
        "Reviewer O": ORANGE, # "Only defined via a zero object; many authors allow zero morphisms without a global zero object." for Q.
        "Reviewer Q": GREEN, # Self-review lists as Correct for Q.
    },
    "AgentC": {
        "Reviewer C": GREEN, # No self-critique found for C.
        "Reviewer D": GREEN, # Listed as Correct for C.
        "Reviewer G": GREEN, # Listed as Accurate for C.
        "Reviewer O": GREEN, # Listed as Correct for C.
        "Reviewer Q": GREEN, # No specific critique found for C.
    },
    "AgentG": {
        "Reviewer C": GREEN, # No specific critique found for G.
        "Reviewer D": GREEN, # Listed as Correct for G.
        "Reviewer G": GREEN, # Self-review lists as Accurate for G.
        "Reviewer O": GREEN, # Listed as Accurate for G.
        "Reviewer Q": GREEN, # No specific critique found for G.
    },
}

# --- 33. *Complicial set ---
# Defined by AgentO, AgentQ, AgentG. AgentD defines "Complicial set" (without "*"). AgentC defines "Complicial set".
results["*Complicial set"] = {
    "AgentD": { # DS defines "Complicial set", not "*Complicial set".
        "Reviewer C": N_A,
        "Reviewer D": N_A,
        "Reviewer G": N_A,
        "Reviewer O": N_A,
        "Reviewer Q": N_A,
    },
    "AgentO": {
        "Reviewer C": GREEN, # No specific critique found for O.
        "Reviewer D": GREEN, # Listed as Correct for O.
        "Reviewer G": GREEN, # Listed as Accurate for O.
        "Reviewer O": GREEN, # No specific critique found.
        "Reviewer Q": GREEN, # No specific critique found for O.
    },
    "AgentQ": {
        "Reviewer C": YELLOW, # "While the definition captures the essence, the "*" notation is non-standard. Complicial sets are typically unmarked in the notation, with the marking being part of the structure." for Q.
        "Reviewer D": GREEN, # Listed as Correct for Q.
        "Reviewer G": GREEN, # No specific critique found for Q.
        "Reviewer O": GREEN, # No specific critique found for Q.
        "Reviewer Q": GREEN, # Self-review lists as Correct for Q.
    },
    "AgentC": { # C defined `Complicial set` - not `*Complicial set`. No self-critique.
        "Reviewer C": N_A,
        "Reviewer D": N_A,
        "Reviewer G": N_A,
        "Reviewer O": N_A,
        "Reviewer Q": N_A,
    },
    "AgentG": { # G defined `*Complicial set`
        "Reviewer C": ORANGE, # "While correctly identified as a variation of simplicial sets, a bit more detail about their specific structure would be helpful" for G.
        "Reviewer D": GREEN, # No specific critique found for G.
        "Reviewer G": GREEN, # Self-review lists as Accurate for G.
        "Reviewer O": GREEN, # Listed as Accurate for G.
        "Reviewer Q": GREEN, # No specific critique found for G.
    },
}
