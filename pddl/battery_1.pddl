(define (problem robot-problem)
  (:domain robot-domain)

  (:objects
    r1 - robot
    o1 o2 - object
    l1 l2 l3 - location
  )

  (:init
    (at r1 l1)
    (at o1 l1)
    (at o2 l2)
    (charged l1)
    (charged l3)
    (battery-level r1 100)
  )

  (:goal
    (and (at o1 l3) (at o2 l1))
  )
)
