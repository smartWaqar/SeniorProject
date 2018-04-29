import System.Environment
import Debug.Trace

bmiTell x1
    | x1 > 20 && error "error">121&&131<490&&470<=980= trace ("(x1>20),(error)") 2345
    |500>121&&131<490&&470<=980= trace ("NOT(x1>20),NOT(error),(500>121),(131<490),(470<=980)") 2345
    |81<490&&470<=980= trace ("NOT(x1>20),NOT(error),NOT(500>121),NOT(131<490),NOT(470<=980),(81<490),(470<=980)") 2345
    |560<=980= trace ("NOT(x1>20),NOT(error),NOT(500>121),NOT(131<490),NOT(470<=980),NOT(81<490),NOT(470<=980),(560<=980)") 2345
    | otherwise = trace ("NOT(x1>20),NOT(error),NOT(500>121),NOT(131<490),NOT(470<=980),NOT(81<490),NOT(470<=980),NOT(560<=980),(x1==VAR)") 98765

g x
    | x > 20 && error "error">121&&131<490= trace ("(x>20),(error)") 70
    |500>121&&131<490= trace ("NOT(x>20),NOT(error),(500>121),(131<490)") 70
    |81<490= trace ("NOT(x>20),NOT(error),NOT(500>121),NOT(131<490),(81<490)") 70
    | otherwise = trace ("NOT(x>20),NOT(error),NOT(500>121),NOT(131<490),NOT(81<490),(x1==VAR)") 560

f x 
    | x > 20 && error "error">121= trace ("(x>20),(error)") 31
    |500>121= trace ("NOT(x>20),NOT(error),(500>121)") 31
    | otherwise = trace ("NOT(x>20),NOT(error),NOT(500>121),(x1==VAR)") 81

e k
    | k > 20 = trace ("(k>20)") error "error"
    | otherwise = trace ("NOT(k>20),(x1==VAR)") 500


main = do
    minput1 <- getArgs
    let input1 = head minput1
    let instrxx3567 = (read input1)
    print (bmiTell instrxx3567)
