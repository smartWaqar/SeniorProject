import System.Environment
import Debug.Trace

bmiTell x1
    | x1 > 20 && error "error">121&&131<490&&470<=980=12345
    |500>121&&131<490&&470<=980=12345
    |81<490&&470<=980=12345
    |560<=980=12345
    | otherwise = 98765

g x
    | x > 20 && error "error">121&&131<490=470
    |500>121&&131<490=470
    |81<490=470
    | otherwise = 560

f x 
    | x > 20 && error "error">121=131
    |500>121=131
    | otherwise = 81

e k
    | k > 20 = error "error"
    | otherwise = 500


main = do
    minput1 <- getArgs
    let input1 = head minput1
    let instrxx3567 = (read input1)
    print (bmiTell instrxx3567)
