(define (problem robowalk_nd_p1)
  (:domain robowalk_nd)

  (:objects
    loc1 loc2 loc3 loc4 loc5
  )

  (:init
    (at loc1)
    (adjacent loc1 loc2)
    (adjacent loc2 loc5)
    (adjacent loc1 loc3)
    (adjacent loc3 loc4)
    (adjacent loc4 loc5)
    (hasrope loc1)
    (hasrope loc3)
    (hasrope loc4)
  )

  (:goal
    (and (at loc5) (not (stuck)))
  )
)
