"""
Asynchronous employees resource for the Holded API.
"""
from typing import Any, Dict, List, Optional, cast

from . import AsyncBaseResource


class AsyncEmployeesResource(AsyncBaseResource):
    """
    Resource for interacting with the Employees API asynchronously.
    """

    async def list(self, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all employees asynchronously.

        Args:
            params: Optional query parameters.

        Returns:
            A list of employees.
        """
        result = await self.client.get("team/employees", params=params)
        return cast(List[Dict[str, Any]], result)

    async def create(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new employee asynchronously.

        Args:
            data: Employee data.

        Returns:
            The created employee.
        """
        result = await self.client.post("team/employees", data=data)
        return cast(Dict[str, Any], result)

    async def get(self, employee_id: str) -> Dict[str, Any]:
        """
        Get a specific employee asynchronously.

        Args:
            employee_id: The employee ID.

        Returns:
            The employee.
        """
        result = await self.client.get(f"team/employees/{employee_id}")
        return cast(Dict[str, Any], result)

    async def update(self, employee_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update an employee asynchronously.

        Args:
            employee_id: The employee ID.
            data: Updated employee data.

        Returns:
            The updated employee.
        """
        result = await self.client.put(f"team/employees/{employee_id}", data=data)
        return cast(Dict[str, Any], result)

    async def delete(self, employee_id: str) -> Dict[str, Any]:
        """
        Delete an employee asynchronously.

        Args:
            employee_id: The employee ID.

        Returns:
            A confirmation message.
        """
        result = await self.client.delete(f"team/employees/{employee_id}")
        return cast(Dict[str, Any], result)

    async def list_time_trackings(self, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all time trackings asynchronously.

        Args:
            params: Optional query parameters.

        Returns:
            A list of time trackings.
        """
        result = await self.client.get("team/timetracking", params=params)
        return cast(List[Dict[str, Any]], result)

    async def get_time_tracking(self, tracking_id: str) -> Dict[str, Any]:
        """
        Get a specific time tracking asynchronously.

        Args:
            tracking_id: The time tracking ID.

        Returns:
            The time tracking.
        """
        result = await self.client.get(f"team/timetracking/{tracking_id}")
        return cast(Dict[str, Any], result)

    async def update_time_tracking(self, tracking_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update a time tracking asynchronously.

        Args:
            tracking_id: The time tracking ID.
            data: Updated time tracking data.

        Returns:
            The updated time tracking.
        """
        result = await self.client.put(f"team/timetracking/{tracking_id}", data=data)
        return cast(Dict[str, Any], result)

    async def delete_time_tracking(self, tracking_id: str) -> Dict[str, Any]:
        """
        Delete a time tracking asynchronously.

        Args:
            tracking_id: The time tracking ID.

        Returns:
            A confirmation message.
        """
        result = await self.client.delete(f"team/timetracking/{tracking_id}")
        return cast(Dict[str, Any], result)

    async def list_employee_time_trackings(self, employee_id: str, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all time trackings for a specific employee asynchronously.

        Args:
            employee_id: The employee ID
            params: Optional query parameters (e.g., page, limit, from, to)

        Returns:
            A list of time trackings for the employee
        """
        result = await self.client.get(f"team", f"employees/{employee_id}/timetracking", params=params)
        return cast(List[Dict[str, Any]], result)

    async def create_employee_time_tracking(self, employee_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a time tracking for a specific employee asynchronously.

        Args:
            employee_id: The employee ID
            data: Time tracking data

        Returns:
            The created time tracking
        """
        result = await self.client.post("team", f"employees/{employee_id}/timetracking", data)
        return cast(Dict[str, Any], result)

    async def employee_clock_in(self, employee_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Clock in an employee asynchronously.

        Args:
            employee_id: The employee ID
            data: Clock in data

        Returns:
            The clock in response
        """
        result = await self.client.post("team", f"employees/{employee_id}/clockin", data)
        return cast(Dict[str, Any], result)

    async def employee_clock_out(self, employee_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Clock out an employee asynchronously.

        Args:
            employee_id: The employee ID
            data: Clock out data

        Returns:
            The clock out response
        """
        result = await self.client.post("team", f"employees/{employee_id}/clockout", data)
        return cast(Dict[str, Any], result) 