(define (domain robowalk_nd)
  (:requirements :strips :probabilistic-effects)
  
  (:predicates
    (at ?loc)           ; the robot is at a location
    (stuck)             ; the robot is stuck
    (adjacent ?loc1 ?loc2) ; two locations are adjacent
    (hasrope ?loc)      ; there's a rope at this location to save stuck robots
  )

  ; Move action: the robot moves from one location to another with some probability of getting stuck.
  (:action move
    :parameters (?from ?to)
    :precondition (and (at ?from) (adjacent ?from ?to) (not (stuck)))
    :effect (probabilistic
                0.6 (and (not (at ?from)) (at ?to))
                0.4 (stuck)   ; 40% chance the robot becomes stuck
            )
  )
  ; Climb action: try to climb rope, which can save you if you are stuck
  (:action climb
    :parameters (?loc)
    :precondition (and (at ?loc) (hasrope ?loc))
    :effect (probabilistic
                0.8 (not (stuck))   ; 80% chance the robot becomes unstuck
                0.2 (stuck)         ; 20% chance the robot remains stuck
            )
  )
)
