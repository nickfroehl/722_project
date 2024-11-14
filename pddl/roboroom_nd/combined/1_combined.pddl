(define (domain roboroom_nd)
  (:requirements :strips :probabilistic-effects)

  (:predicates
    (at ?room)              ; Robot is at a specific room
    (connected ?room1 ?room2) ; Rooms are connected
  )

  (:action move
    :parameters (?from ?to)
    :precondition (and (at ?from) (connected ?from ?to))
    :effect (probabilistic
      0.7 (and (not (at ?from)) (at ?to)) ; 70% chance to move successfully
      0.3 (at ?from)                      ; 30% chance to stay in the same room
    )
  )
)
(define (problem roboroom_nd_p1)
  (:domain roboroom_nd)

  (:objects
    room1 room2 room3  ; Define the rooms
  )

  (:init
    (at room1)
    (connected room1 room2)
    (connected room2 room3)
  )

  (:goal
    (at room3)
  )
)
