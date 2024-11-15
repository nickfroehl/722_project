
(define (domain robowalk_nd)
  (:requirements :typing)
  (:types default)
  
  (:predicates (at ?v0 - default)
	(stuck)
	(adjacent ?v0 - default ?v1 - default)
	(hasrope ?v0 - default)
  )
  ; (:actions climb move)

  

	(:action move
		:parameters (?from - default ?to - default)
		:precondition (and (at ?from)
			(adjacent ?from ?to)
			(not (stuck)))
		:effect (and
			(not (at ?from))
			(at ?to))
	)
	

	(:action climb
		:parameters (?loc - default)
		:precondition (and (at ?loc)
			(hasrope ?loc))
		:effect (not (stuck))
	)

  

)
        