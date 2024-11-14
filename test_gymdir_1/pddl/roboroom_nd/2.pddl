(define (problem roboroom_nd_p2)
  (:domain roboroom_nd)
  
  (:objects
    room1 room2 room3 room4 room5 room6 room7 room8
  )

  (:init
    (at room1)
    (connected room1 room2)
    (connected room2 room3)
    (connected room3 room4)
    (connected room4 room5)
    (connected room5 room6)
    (connected room6 room7)
    (connected room7 room8)
    (connected room2 room5)
    (connected room5 room7)
    (connected room4 room8)
  )

  (:goal
    (at room8)
  )
)