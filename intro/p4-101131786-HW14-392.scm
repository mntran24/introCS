;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname p4-101131786-HW14-392) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;Team LSAT Roster: Malk, Gabriel, Mai
;IntroCS pd04 sec04
;HW14 -- Hack
;2022-10-12
;Time cost: 1 hr
;(getOnesDigit n) returns the ones digit of its single integer parameter.
(define getOnesDigit
  (lambda (n)
   (abs (remainder n 10))))
(getOnesDigit 34)
"...should be 4"
(getOnesDigit -258)
"...should be 8"
(getOnesDigit 3670)
"...should be 0"
(getOnesDigit 2)
"...should be 2"
(getOnesDigit 99999)
"...should be 9"
(getOnesDigit 457)
"...should be 7"
;(discriminant a b c) takes three inputs, representing (in order) the coefficients of a quadratic equation in standard form.
;Returns the value of the discriminant of the equation.
(define discriminant
  (lambda (a b c)
    (- (sqr b)
       (* 4 a c))))
(discriminant 4 2 2)
"...should be -28"
(discriminant 2 4 2)
"...should be 0"
(discriminant 5 10 3)
"...should be 40"
(discriminant -5 4 7)
"...should be 156"
(discriminant -8 -3 -9)
"...should be -279"
;(root1 a b c) takes three inputs, representing (in order) the coefficients of a quadratic equation in standard form.
;Returns a root of the equation (the “plus” root, meaning the equation will be (-b+sqrt(b^2-4ac))/2a).
(define root1
  (lambda (a b c)
    (/ (- (sqrt (discriminant a b c))
          b)
       (* 2 a))))
(root1 2 4 2)
"should be -1"
(root1 1 -6 9)
"...should be 3"
(root1 4 8 12)
"...should be -1+1.41421i"
(root1 3 9 8)
"...should be -1.5+0.645497i"
(root1 8 99 1)
"...should be -0.010109"
;(getHundredsDigit n) returns the hundreds digit of its single integer input.
(define getHundredsDigit
  (lambda (x)
    (getOnesDigit
     (/ (abs (- x
                (remainder x 100)))
        100))))
(getHundredsDigit 234)
"...should be 2"
(getHundredsDigit 76348)
"...should be 3"
(getHundredsDigit -5839)
"...should be 8"
(getHundredsDigit 13274691)
"...should be 6"
(getHundredsDigit 99)
"...should be 0"
(getHundredsDigit 0)
"...should be 0"
;(disaster a b c) returns how long (in hours) it will take for two trains, initially separated by distance c, in miles, to crash into each other.
;The trains are traveling toward one another on the same track, at speeds a and b, in miles per hour.
;formula used: time = distance/sum of the speeds
(define disaster
  (lambda (a b c)
    (/ c
       (+ a b))))
(disaster 20 80 100)
"...should be 1"
(disaster 4 2 30)
"...should be 5"
(disaster 30 90 200)
"...should be 1.666666"
(disaster 1 0 200)
"...should be 200"
(disaster 100 -90 300)
"...should be 30"
(disaster 2 7 33)
"...should be 3.6666"