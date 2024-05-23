;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname hw16) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;Mai Tran
;IntroCS pd04 sec04
;HW16 -- If statement: # of real solutions to quadratic equation
;2022-10-16
;Time cost: 0.5 hr
;consulted: Malk, Gabriel
;(discriminant a b c) takes in the 3 coefficients of a quadratic equation (in order) and returns the discriminant, b^2-4ac.
(define discriminant
  (lambda (a b c)
    (- (sqr b)
       (* 4 a c))))
(discriminant 4 2 2)
"...should be -28"
(discriminant 2 4 2)
"...should be 0"
(discriminant 5 10 3)
"...should be 40"
(discriminant -5 4 7)
"...should be 156"
(discriminant -8 -3 -9)
"...should be -279"
;(quadSolve a b c) takes in the 3 coefficients of a quadratic equation (in order) and returns the number of real solutions to the equation.
;The function uses the discriminant (D) to determine the number of real solutions.
;If D>0 -> 2 real solutions; D<0 -> 0 real solutions; D=0 -> 1 real solution.
(define quadSolve
  (lambda (a b c)
    (if (> (discriminant a b c) 0)
    2
    (if (< (discriminant a b c) 0)
        0 1))))
(quadSolve 4 2 2)
"...should be 0"
(quadSolve 2 4 2)
"...should be 1"
(quadSolve 5 10 3)
"...should be 2"
(quadSolve -5 4 7)
"...should be 2"
(quadSolve -8 -3 -9)
"...should be 0"

