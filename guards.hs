import System.Environment
import Debug.Trace

bmiTell x1
    | g x1 <= 980 = 12345
    | otherwise = 98765

g x
    | f x < 490 = 470
    | otherwise = 560

f x 
    | e x > 121 = 131
    | otherwise = 81

e k
    | k > 20 = error "error"
    | otherwise = 500


main = do
    minput1 <- getArgs
    let input1 = head minput1
    let instrxx3567 = (read input1)
    print (bmiTell instrxx3567)
