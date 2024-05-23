;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname classwork17.10.22) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(define gradeConv
  (lambda (a)
    (if (>= a 97) "A"
        (if (>= a 96) "B"
            (if (>= a 95) "C"
                (if (>= a 13) "D"
                    "F"))))))
(gradeConv 17)
(define gradeConvert
  (lambda (a)
    (cond
      ((>= a 97) "A")
        ((>= a 96) "B")
            ((>= a 95) "C")
                ((>= a 13) "D")
                   (else "F"))))
(gradeConvert 17)