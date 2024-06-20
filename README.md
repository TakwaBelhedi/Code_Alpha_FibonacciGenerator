I've recently completed my first task at CodeAlpha: developing a 𝐅𝐢𝐛𝐨𝐧𝐚𝐜𝐜𝐢 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐨𝐫! 🌟 The Fibonacci series is a sequence where each number is the sum of the two preceding ones. Throughout this project, I learned fundamental programming concepts:

𝐑𝐞𝐜𝐮𝐫𝐬𝐢𝐨𝐧: is a programming technique where a function calls itself repeatedly till a termination condition is met. But the issue with them is that in the recursion tree, there can be chances that the sub-problem that is already solved is being solved again, which adds to overhead.

𝐌𝐞𝐦𝐨𝐢𝐳𝐚𝐭𝐢𝐨𝐧: is a technique of recording the intermediate results so that it can be used to avoid repeated calculations and speed up the programs. It can be used to optimize the programs that use recursion. In Python, memoization can be done with the help of function decorators.

Initially, I worked with the recurrence relation: 𝐟𝐢𝐛𝐨𝐧𝐚𝐜𝐜𝐢(𝐧) = 𝐟𝐢𝐛𝐨𝐧𝐚𝐜𝐜𝐢(𝐧-𝟏) + 𝐟𝐢𝐛𝐨𝐧𝐚𝐜𝐜𝐢(𝐧-𝟐). As I addressed larger calculations like fibonacci(1000), I encountered RecursionError: maximum recursion depth exceeded, which I resolved using a GeeksforGeeks article: https://www.geeksforgeeks.org/python-handling-recursion-limit/
