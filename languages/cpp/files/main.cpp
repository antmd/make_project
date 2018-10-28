#include <iostream>

#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>

using namespace std;





SCENARIO("Basic Usage", "[Vector]")
{
        GIVEN("An empty vector")
        {
                vector<int> buf;

                REQUIRE(buf.empty());

                WHEN("An item is inserted")
                {
                        buf.push_back(3);

                        THEN("The count is one")
                        {
                                REQUIRE(buf.size() == 1);
                        }
                }

                WHEN("Cleared")
                {
                        buf.push_back(5);
                        buf.clear();

                        THEN("Empty")
                        {
                                REQUIRE(buf.size() == 0);
                        }
                }

        }
}
