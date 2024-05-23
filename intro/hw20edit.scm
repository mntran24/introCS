;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname hw20edit) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(define sumPtoQ
  (lambda (p q)
    (if (< p q)
        (+ p (sumPtoQ (+ p 1) q))
        p)))
(sumPtoQ 2 3)
"...should be 5"