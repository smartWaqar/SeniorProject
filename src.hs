import System.Environment
import Debug.Trace

factorial 0 = error "error"
factorial 1 = 2
factorial n = n * factorial (n - 1)


--main = print (factorial 5)

main = do
       --putStrLn "enter value for x: "
       --input1 <- getLine
       minput1 <- getArgs
       let input1 = head minput1
       let instrxx3567 = (read input1 :: Int)
       print (factorial instrxx3567)