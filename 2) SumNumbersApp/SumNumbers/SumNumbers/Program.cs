using System;
using System.Diagnostics;

class Program
{
    static void Main()
    {
        bool tryAgain = true;
        do
        {
            long number = GetNumber();
            Console.WriteLine($"\nCalculating sum from 1 to {number:N0}...\n");

            Stopwatch timer1 = Stopwatch.StartNew();

            long sumLoop = CalculateWithLoop(number);

            timer1.Stop();


            Stopwatch timer2 = Stopwatch.StartNew();

            long sumFormula = CalculateWithFormula(number);

            timer2.Stop();

            Console.WriteLine("RESULTS:");
            Console.WriteLine($"Loop result: {sumLoop:N0}");
            Console.WriteLine($"Formula result: {sumFormula:N0}");
            Console.WriteLine($"Loop method took: {timer1.Elapsed.TotalSeconds:F6} seconds");
            Console.WriteLine($"Formula method took: {timer2.Elapsed.TotalSeconds:F6} seconds");

            Console.Write("\nDo you want to try another number? (y/n): ");

            string? response = Console.ReadLine()?.ToLower();
            if (response != "y" && response != "yes")
            {
                tryAgain = false;
            }

            Console.WriteLine();

        } while (tryAgain);

        Console.WriteLine("Thank you -_-");
    }

    static long GetNumber()
    {
        while (true)
        {
            Console.Write("Enter a positive number: ");
            string? input = Console.ReadLine();

            if (string.IsNullOrEmpty(input))
            {
                Console.WriteLine("Please enter something!");
                continue;
            }

            if (!long.TryParse(input, out long number))
            {
                Console.WriteLine("That's not a valid number!");
                continue;
            }

            if (number <= 0)
            {
                Console.WriteLine("Please enter a positive number!");
                continue;
            }

            return number;
        }
    }

    static long CalculateWithLoop(long number)
    {
        long sum = 0;
        for (long iterator = 1; iterator <= number; iterator++)
        {
            sum += iterator;
        }
        return sum;
    }

    static long CalculateWithFormula(long number)
    {
        return number * (number + 1) / 2;
    }
}