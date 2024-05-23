;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname pythtriples) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))

(define isPythTriple?
  (lambda (a b c) (
    (= (sqr c) (+ (sqr a) (sqr b)))))
(isPythTriple? 3 4 5)
"...should be #true"
(isPythTriple? 3 5 4)
"...should be #true"
(isPythTriple? 3 4 5)
"...should be #true"
(isPythTriple? 3 4 5)
"...should be #true"
(isPythTriple? 3 4 5)
"...should be #true"