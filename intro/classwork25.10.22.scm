;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname classwork25.10.22) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(define sumOdd
  (lambda (n)
    (if (> n 0)
        (if (= (remainder n 2) 0)
            (sumOdd (- n 1))
            (+ n (sumOdd (- n 2))))
        0)))
(sumOdd 0)
(sumOdd 1)
(sumOdd 2)
(sumOdd 3)
(sumOdd 9)
(sumOdd 10)
