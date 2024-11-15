(define (domain robot-domain)
  (:requirements :strips :typing :fluents)

  (:types
    location
    object
  )

  (:predicates
    (at ?r - robot ?l - location)
    (has ?r - robot ?o - object)
    (charged ?l - location)
  )

  (:functions
    (battery-level ?r - robot)
  )

  (:action move
    :parameters (?r - robot ?from - location ?to - location)
    :precondition (and (at ?r ?from))
    :effect (and (not (at ?r ?from)) (at ?r ?to) (decrease (battery-level ?r) 10)))
  )

  (:action pickup
    :parameters (?r - robot ?o - object ?l - location)
    :precondition (and (at ?r ?l) (at ?o ?l))
    :effect (and (has ?r ?o) (not (at ?o ?l)) (decrease (battery-level ?r) 5)))
  )

  (:action drop
    :parameters (?r - robot ?o - object ?l - location)
    :precondition (and (at ?r ?l) (has ?r ?o))
    :effect (and (not (has ?r ?o)) (at ?o ?l) (decrease (battery-level ?r) 2)))
  )

  (:action recharge
    :parameters (?r - robot ?l - location)
    :precondition (and (at ?r ?l) (charged ?l))
    :effect (increase (battery-level ?r) 50))
)