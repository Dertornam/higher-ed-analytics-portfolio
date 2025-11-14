* Example SPSS syntax: recode educational goals to CSCE / GRAD / OTHER.

VALUE LABELS DEMOG7
 1 'Associate degree'
 2 "Bachelor's degree"
 3 "Master's degree"
 4 "Doctorate or professional degree"
 5 'Certification (initial or review)'
 6 'Self-improvement/pleasure'
 7 'Job-related training'
 8 'Other educational goal'
 0 "Missing/Not Available".

RECODE DEMOG7
 (1,2,5,6,7 = 1)   /* CSCE */
 (3,4 = 2)        /* GRAD */
 (8 = 3)          /* OTHER */
 (0, SYSMIS = SYSMIS) INTO GOAL_CAT.
VARIABLE LABELS GOAL_CAT 'Educational Goal Category (1=CSCE,2=GRAD,3=OTHER)'.
VALUE LABELS GOAL_CAT 1 'CSCE' 2 'GRAD' 3 'OTHER'.

EXECUTE.

* Example: compute item means and performance gaps if items are named I01_I (importance) and I01_S (satisfaction).
