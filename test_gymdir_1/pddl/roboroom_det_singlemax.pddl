
(define (domain roboroom_nd)
  (:requirements :typing)
  (:types default)
  
  (:predicates (at ?v0 - default)
	(connected ?v0 - default ?v1 - default)
  )
  ; (:actions move)

  

	(:action move
		:parameters (?from - default ?to - default)
		:precondition (and (at ?from)
			(connected ?from ?to))
		:effect (and
			(not (at ?from))
			(at ?to))
	)

  

)
        