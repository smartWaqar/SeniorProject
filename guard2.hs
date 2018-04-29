import System.Environment
import Debug.Trace

bmiTell x1
    | g x1 <= 18.5 = 18.5
    | otherwise = 58.0

g x
    | f x < 11 = 21
    | otherwise = 111

f x 
    | e x >121 = 131
    | otherwise = x

e k
    | k > 999 = 233
    | otherwise = 989


main = do
    minput1 <- getArgs
    let input1 = head minput1
    let instrxx3567 = (read input1)
    print (bmiTell instrxx3567)
