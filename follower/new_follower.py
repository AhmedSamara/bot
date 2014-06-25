"""2015 IEEE SEcon line following code-base."""

import lib.lib as lib
import hardware.ir_hub as ir_hub_mod
import driver.mec_driver as mec_driver_mod

class NewFollower(object):
    
    """Follows a line, detects intersections."""
    
    def __init__(self):
        # Build logger
        self.logger = lib.get_logger()
        
        # Build sub-system objs.
        self.ir_hubs = ir_hub_mod.IRHub()
        self.driver = mec_driver_mod.MecDriver()

    @lib.api_call
    def follow(self):
        """Main entry point for defining simple-case line following."""
        
        self.logger.debug("follower entry")