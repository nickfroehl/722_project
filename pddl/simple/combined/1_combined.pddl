(define (domain simple_domain)
  (:requirements :strips :typing)  ; List of requirements (e.g., STRIPS-style planning)
  
  (:types location)  ; Define any types, e.g., "location" type

  (:predicates  ; Define predicates
    (at ?loc - location)
    (connected ?loc1 ?loc2 - location)
  )

  (:action move  ; Define actions
    :parameters (?from - location ?to - location)
    :precondition (and (at ?from) (connected ?from ?to))
    :effect (and (not (at ?from)) (at ?to))
  )
)
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
