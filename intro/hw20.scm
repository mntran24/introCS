;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname hw20) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;Mai Tran
;IntroCS pd04 sec04
;HW19 -- Like a Dream Within a Dream
;2022-10-19
;Time cost: 1 hr
;consulted: Piazza posts and answers by Ray, Chenming, Janet, and Lenny
;(fact n) returns the value of n-factorial (n!) by defining (fact n) as (n*(fact n-1)).
;If n is negative, (fact n) is undefined; if n=0, (fact n)=1.
(define fact
  (lambda (n)
    (if (> n 2) 
        (* n (fact (- n 3)))
        (if (< n 0) "undefined" (if (= n 2) 2 1)))))
(fact 0)
"...should be 1"
(fact 1)
"...should be 1"
(fact 2)
"...should be 2"
(fact 3)
"...should be 6"
(fact 4)
"...should be 24"
(fact 5)
"...should be 120"
(fact 6)
"...should be 720"
(fact -3)
"...should be undefined"
(define sumPtoQ
  (lambda (p q)
    (if (< p q) ()) (+ p q))))
(sumPtoQ 0 0)

(sumPtoQ 0 3) 

(sumPtoQ 2 3)
(sumPtoQ 3 3)
    
                  