using System;
using System.Text;
using System.Diagnostics;

internal class Program
{
    static void Main(string[] args)
    {
        bool tryAgain = true;
        do
        {
            int maximumNumber = GetMaximumNumber();

            Console.WriteLine($"\nGenerating numbers from 1 to {maximumNumber:N0}...\n");

            Stopwatch timer1 = Stopwatch.StartNew();
            string numbersWithStringBuilder = GenerateNumbersWithStringBuilder(maximumNumber);
            timer1.Stop();

            Stopwatch timer2 = Stopwatch.StartNew();
            string numbersWithoutStringBuilder = GenerateNumbersWithoutStringBuilder(maximumNumber);
            timer2.Stop();


            Console.WriteLine($"Generated numbers up to {maximumNumber:N0} using String Builder:");
            Console.WriteLine(numbersWithStringBuilder);

            Console.WriteLine();
            Console.WriteLine();

            Console.WriteLine($"Generated numbers up to {maximumNumber:N0} using String Concatenation:");
            Console.WriteLine(numbersWithoutStringBuilder);

            Console.WriteLine();
            Console.WriteLine();

            Console.WriteLine("PERFORMANCE RESULTS:");
            Console.WriteLine($"StringBuilder method took: {timer1.Elapsed.TotalSeconds:F6} seconds");
            Console.WriteLine($"String concatenation method took: {timer2.Elapsed.TotalSeconds:F6} seconds");

            if (timer2.Elapsed.TotalSeconds > 0)
            {
                double speedup = timer2.Elapsed.TotalSeconds / timer1.Elapsed.TotalSeconds;
                Console.WriteLine($"StringBuilder is {speedup:F2}x faster!\n");
            }



            Console.WriteLine();
            Console.WriteLine();

            Console.Write("Do you want to try another number? (y/n): ");
            string? response = Console.ReadLine()?.ToLower();
            if (response != "y" && response != "yes")
            {
                tryAgain = false;
            }
            Console.WriteLine();
        } while (tryAgain);

        Console.WriteLine("Thank you -_-");
    }

    static int GetMaximumNumber()
    {
        while (true)
        {
            Console.Write("Enter the maximum positive number you need to write: ");
            string? input = Console.ReadLine();

            if (string.IsNullOrWhiteSpace(input))
            {
                Console.WriteLine("Input cannot be empty. Please enter a number!");
                continue;
            }

            if (!int.TryParse(input, out int number))
            {
                Console.WriteLine("That's not a valid number. Please enter an integer!");
                continue;
            }

            if (number <= 0)
            {
                Console.WriteLine("Please enter a positive number (greater than 0)!");
                continue;
            }


            return number;
        }
    }

    static string GenerateNumbersWithStringBuilder(int maximumNumber)
    {
        StringBuilder stringBuilder = new StringBuilder();
        for (int iterator = 1; iterator <= maximumNumber; iterator++)
        {
            stringBuilder.Append(iterator);
            if (iterator < maximumNumber)
            {
                stringBuilder.Append(",");
            }
        }
        return stringBuilder.ToString();
    }

    static string GenerateNumbersWithoutStringBuilder(int maximumNumber)
    {
        string result = "";
        for (int iterator = 1; iterator <= maximumNumber; iterator++)
        {
            result += iterator.ToString();
            if (iterator < maximumNumber)
            {
                result += ",";
            }
        }
        return result;
    }
}