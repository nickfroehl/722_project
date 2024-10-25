(define (problem simple_problem)
  (:domain simple_domain)  ; Must match the domain name in the operator file

  (:objects  ; List all objects used in the problem
    loc1 loc2 loc3 - location
  )

  (:init  ; Define initial state
    (at loc1)
    (connected loc1 loc2)
    (connected loc2 loc3)
  )

  (:goal  ; Define goal state
    (at loc3)
  )
)
