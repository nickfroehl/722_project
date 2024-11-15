(define (domain nested_nd)
  (:requirements :strips :probabilistic-effects)

  (:predicates
    (at ?loc)
    (adjacent ?loc1 ?loc2)
    (p1)
    (p2)
    (p3)
    (p4)
    (p5)
  )

  (:action prob-action
    :parameters (?from ?to)
    :precondition (and (at ?from) (adjacent ?from ?to))
    :effect (and
      (probabilistic
        (0.5 (p1))
        (0.5 (p2))
      )
      (probabilistic
        (0.3 (p3))
        (0.7 (and (p4) (p5)))
      )
      (and (not (at ?from)) (at ?to))
    )
  )
)