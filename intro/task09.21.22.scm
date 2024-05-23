;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname task09.21.22) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
; the stepper works by reading the definitions window and seeing if the definitions can be successfully evaluated.
; it checks the syntax, the variable, and the value, and if there are any errors, the stepper creates a log of the errors so that the programmer knows where their mistakes are.
(define foo (lambda (d) d))
(foo 3)
"... should be 3"
(define AreaCirc (lambda (R) (* pi (expt R 2))))
(AreaCirc 3)
"... should be 28"
(define areaCirc (lambda (R) pi))
(areaCirc 1)
"...should be 3.14"
(define AreaWasher (lambda (R1) (R2)) (* pi))
(AreaWasher 1 3)
"...should be 25.12"