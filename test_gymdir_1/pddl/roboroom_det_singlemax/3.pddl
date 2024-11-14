(define (problem roboroom_nd_p1)
  (:domain roboroom_nd)

  (:objects
    room1 room2 room3 room4 ; Define the rooms
  )

  (:init
    (at room1)
    (connected room1 room2)
    (connected room2 room3)
  )
  ; NO SOLUTION
  (:goal
    (at room4)
  )
)
