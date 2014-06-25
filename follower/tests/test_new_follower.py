"""Test cases for new_follower."""

import unittest
import follower.new_follower as nf_mod
import tests.test_bot as test_bot

class TestFollower(test_bot.TestBot):

    """Tests main entry point for new line Follower."""
    
    def setUp(self):
        """Builds config and IR objects."""
        super(TestFollower, self).setUp()
        
        # Build follower object.
        self.follower = nf_mod.NewFollower()
        
    def tearDown(self):
        """Calls super-class teardown."""
        super(TestFollower, self).tearDown()
    
    def test_basic(self):
        """Basic call to test entry to follower."""
        self.follower.follow()