(define (domain simple_domain)
  (:requirements :strips :typing)  ; List of requirements (e.g., STRIPS-style planning)
  
  (:types location)  ; Define any types, e.g., "location" type

  (:predicates  ; Define predicates
    (at ?loc - location)
    (connected ?loc1 - location ?loc2 - location)
  )

  (:action move  ; Define actions
    :parameters (?from - location ?to - location)
    :precondition (and (at ?from) (connected ?from ?to))
    :effect (and (not (at ?from)) (at ?to))
  )
)
