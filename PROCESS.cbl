       IDENTIFICATION DIVISION.
       PROGRAM-ID. PROCESS.
       
       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT DAILY-FILE ASSIGN TO 'daily_file.txt'
                  ORGANIZATION IS LINE SEQUENTIAL.

           SELECT OUT-FILE ASSIGN TO 'daily_update_file.txt'
                  ORGANIZATION IS LINE SEQUENTIAL.
       
       DATA DIVISION.
       FILE SECTION.
       FD  DAILY-FILE.
       01  DAILY-RECORD.
           05 LOAN-ID          PIC X(03).
           05 FILLER           PIC X.
           05 LOAN-AMOUNT      PIC 9(12).
           05 FILLER           PIC X.
           05 LOAN-LEFT        PIC 9(12).
           05 FILLER           PIC X.
           05 LOAN-TERM        PIC X(2).
           05 FILLER           PIC X.
           05 LOAN-COMPLETED   PIC X.

       FD  OUT-FILE.
       01  OUTPUT-RECORD.
           05 OUT-LOAN-ID          PIC X(03).
           05 FILLER               PIC X.
           05 OUT-LOAN-AMOUNT      PIC 9(12).
           05 FILLER               PIC X.
           05 OUT-LOAN-LEFT        PIC 9(12).
           05 FILLER               PIC X.
           05 OUT-LOAN-TERM        PIC X(2).
           05 FILLER               PIC X.
           05 OUT-LOAN-COMPLETED   PIC X.
       
       WORKING-STORAGE SECTION.
       01  WS-EOF           PIC X VALUE 'N'.
       01  WS-READ-CODE     PIC 99.
       01  EMI PIC 9(12) VALUE ZEROS.
       01  WS-TEMP       PIC 9(12).
       
       PROCEDURE DIVISION.
       BEGIN.
           OPEN INPUT DAILY-FILE
           OPEN OUTPUT OUT-FILE
           PERFORM PROCESS-LOAN UNTIL WS-EOF = 'Y'
           CLOSE DAILY-FILE
           STOP RUN.
       
       PROCESS-LOAN.
           READ DAILY-FILE
                AT END MOVE 'Y' TO WS-EOF
                NOT AT END
      *          DISPLAY "LOAN TERM : " LOAN-TERM
                 DIVIDE LOAN-AMOUNT BY LOAN-TERM GIVING EMI
                   
                   COMPUTE WS-TEMP = LOAN-LEFT - EMI 

                    IF WS-TEMP = ZERO OR LOAN-LEFT = ZERO
                       MOVE DAILY-RECORD TO OUTPUT-RECORD
                       MOVE WS-TEMP TO OUT-LOAN-LEFT
                       MOVE LOAN-LEFT TO OUT-LOAN-AMOUNT
                      
                       MOVE 'Y' TO OUT-LOAN-COMPLETED
                       WRITE OUTPUT-RECORD
                    ELSE 
                       MOVE DAILY-RECORD TO OUTPUT-RECORD
                       MOVE WS-TEMP TO OUT-LOAN-LEFT
                       SUBTRACT 1 FROM OUT-LOAN-TERM
                       MOVE LOAN-LEFT TO OUT-LOAN-AMOUNT
                      
                       
                       WRITE OUTPUT-RECORD
                       
           END-READ.
       