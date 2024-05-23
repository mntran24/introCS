;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname hw08teamwork) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;TPNG: Lsat Roster: Mai, Malk, Gabriel
;IntroCS pd4
;HW08 -- Spoken Word to Coded Form
;2022-09-30
(define ArithMean3
  (lambda (a b c)
    (/ (+ a b c) 3)))
(ArithMean3 1 2 3)
"...2"
(define HarMean3
  (lambda (a b c)
    (/ 1 (/ (+ (/ 1 a) (/ 1 b) (/ 1 c)) 3))))
(HarMean3 3 6 18)
"...5.4"
(define CartDist
  (lambda (X1 Y1 X2 Y2)
    (sqrt (+ (expt (- X2 X1) 2) (expt (- Y2 Y1) 2)))))
(CartDist 0 0 3 4)
"...5"
(define MAX2
  (lambda (a b)
    (+ (/ (+ a b) 2) (abs (/ (- a b) 2)))))
(MAX2 8 9)
"...9"