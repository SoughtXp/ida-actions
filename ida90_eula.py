#!/usr/bin/env python3
import getpass

import ida_registry

## Agree to EULA using this simple hack.
## Fall back to getpass.getuser() when the USER env var is not exported
## (e.g. on CI runners), so the registry key is never written as "None".
user = getpass.getuser()
ida_registry.reg_write_int(f"EULA 90 {user}", 1, "")
