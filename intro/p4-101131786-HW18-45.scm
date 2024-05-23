;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname p4-101131786-HW18-45) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;Mai Tran
;IntroCS pd04 sec04
;HW18 -- Picking the Right Tool for the Job
;2022-10-18
;Time cost: 1 hr
;consulted: Andrew Choi
;(isLeapYr year) returns true if year is a leap year, false otherwise, according to these rules:
;Generally, a year divisible by 4 is a leap year. However, century years are not leap years unless they are divisible by 400.
(define isLeapYr
  (lambda (year)
    (cond
      ((= (remainder year 400) 0) true)
      ((= (remainder year 100) 0) false)
      ((= (remainder year 4) 0) true)
      (else false))))
(isLeapYr 2000)
"...should be true"
(isLeapYr 2004)
"...should be true"
(isLeapYr 2008)
"...should be true"
(isLeapYr 2009)
"...should be false"
(isLeapYr 2100)
"...should be false"
(isLeapYr 2104)
"...should be true"
(isLeapYr 2200)
"...should be false"
(isLeapYr 2300)
"...should be false"
(isLeapYr 2400)
"...should be true"
"here the alt implementation starts"
;an alternate implementation of (isLeapYr year)
;this follows the same logic as above, with perhaps a more compact conditional?
(define isLeapYr?
  (lambda (year)
     (or (= (remainder year 400) 0)
         (and (not (= (remainder year 100) 0)) (= (remainder year 4) 0)))))
(isLeapYr? 2000)
"...should be true"
(isLeapYr? 2004)
"...should be true"
(isLeapYr? 2008)
"...should be true"
(isLeapYr? 2009)
"...should be false"
(isLeapYr? 2100)
"...should be false"
(isLeapYr? 2104)
"...should be true"
(isLeapYr? 2200)
"...should be false"
(isLeapYr? 2300)
"...should be false"
(isLeapYr? 2400)
"...should be true"
;(daysInMonth month year) takes numeric inputs month and year and returns the number of days in the month specified.
;Assumes month is an integer from 1 to 12 and year is a 4-digit positive integer.
(define daysInMonth
  (lambda (month year)
    (cond
      ((= month 2) (if (isLeapYr year) 29 28))
      ((or (= month 4) (= month 6) (= month 9) (= month 11)) 30)
      (else 31))))
(daysInMonth 1 2010)
"...should be 31"
(daysInMonth 2 2011)
"...should be 28"
(daysInMonth 2 2000)
"...should be 29"
(daysInMonth 4 2011)
"...should be 30"
(daysInMonth 9 2008)
"...should be 30"
(daysInMonth 2 1900)
"...should be 28"