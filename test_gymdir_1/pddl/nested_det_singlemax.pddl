
(define (domain nested_nd)
  (:requirements :typing)
  (:types default)
  
  (:predicates (at ?v0 - default)
	(adjacent ?v0 - default ?v1 - default)
	(p1)
	(p2)
	(p3)
	(p4)
	(p5)
  )
  ; (:actions prob-action)

  

	(:action prob-action
		:parameters (?from - default ?to - default)
		:precondition (and (at ?from)
			(adjacent ?from ?to))
		:effect (and
			(p1)
			(and
			(p4)
			(p5))
			(and
			(not (at ?from))
			(at ?to)))
	)

  

)
        