;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname p4-101131786-HW11-427) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;Mai Tran
;IntroCS pd04 sec04
;HW11 -- Seeking Truth
;2022-10-04
;Time cost: 1 hr
;Collaborated with: N/A
;Consulted: Gabriel, Malk
(define XOR
  (lambda (a b)
    (and (not (and a b)) (or a b))))
(XOR #t #f)
"...should be #true"
(XOR #t #t)
"...should be #false"
(XOR #f #f)
"...should be #false"
;(XOR a b) accepts arguments a, b and only returns true if exactly one input is true.
;(not (and a b)) returns true when at least one argument is false, (or a b) returns true when at least one argument is true.
;the two combined together ensures that true is returned when one argument is true and the other is false.
(define bic
  (lambda (a b)
    (not (XOR a b))))
(bic #f #f)
"...should be #true"
(bic #t #t)
"...should be #true"
(bic #t #f)
"...should be #false"
;(bic a b) accepts arguments a, b and returns true if both have the same truth value, false otherwise.
;since (XOR a b) returns true when the two arguments are distinct => (bic a b) is the negation of (XOR a b).
(define XOR3
  (lambda (a b c)
    (and (or a b c) (and (not (and a b)) (not (and b c)) (not (and a c))))))
(XOR3 #t #t #t)
"...should be #f"
(XOR3 #t #t #f)
"...should be #f"
(XOR3 #t #f #t)
"...should be #f"
(XOR3 #t #f #f)
"...should be #t"
(XOR3 #f #t #t)
"...should be #f"
(XOR3 #f #t #f)
"...should be #t"
(XOR3 #f #f #t)
"...should be #t"
(XOR3 #f #f #f)
"...should be #f"
;(XOR3 a b c) accepts arguments a, b, c and returns true if only one value is true, false otherwise.
;similar to with (not (and a b)), (and (not (and a b)) (not (and b c)) (not (and a c))) checks if any two arguments are true
;and only returns true if no two arguments are true.
;(or a b c) checks if at least one argument is true and only returns true if that is fulfilled.
;the two combined only returns true if only one argument is true.
(define XOR3s
  (lambda (a b c)
    (and (not (and a b c)) (XOR c (XOR a b)))))
(XOR3s #t #t #t)
"...should be #f"
(XOR3s #t #t #f)
"...should be #f"
(XOR3s #t #f #t)
"...should be #f"
(XOR3s #t #f #f)
"...should be #t"
(XOR3s #f #t #t)
"...should be #f"
(XOR3s #f #t #f)
"...should be #t"
(XOR3s #f #f #t)
"...should be #t"
(XOR3s #f #f #f)
"...should be #f"
