;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname revisedPythTriple) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(define pyth
  (lambda (a b c)
    (= (+ (* a a)
          (* b b))
       (* c c))))
(define isPythTriple?
  (lambda (a b c)
    (or (pyth a b c)
        (pyth b c a)
        (pyth a c b))))
(isPythTriple? 4 3 5)