(define (problem nested_nd_1)
  (:domain nested_nd)

  (:objects
    room1 room2  ; Define the rooms
  )

  (:init
    (at room1)
    (adjacent room1 room2)
    (adjacent room2 room1)
  )

  (:goal
    (and (p1) (p4))
  )
)