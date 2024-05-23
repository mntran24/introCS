;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname remainderisodd10.11.22) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(define ISODD (lambda (x) (= 1 (modulo x 2))))
(ISODD 3)
(define isodd (lambda (x) (= 1 (remainder x 2))))
(isodd 3)