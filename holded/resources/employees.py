"""
Employees resource for the Holded API.
"""
from typing import Any, Dict, List, Optional, cast

from . import BaseResource


class EmployeesResource(BaseResource):
    """
    Resource for interacting with the Employees API.
    """

    def list(self, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all employees.

        Args:
            params: Optional query parameters (e.g., page, limit)

        Returns:
            A list of employees
        """
        return cast(List[Dict[str, Any]], self.client.get("team", "employees", params=params))

    def create(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new employee.

        Args:
            data: Employee data

        Returns:
            The created employee
        """
        return cast(Dict[str, Any], self.client.post("team", "employees", data))

    def get(self, employee_id: str) -> Dict[str, Any]:
        """
        Get a specific employee.

        Args:
            employee_id: The employee ID

        Returns:
            The employee details
        """
        return cast(Dict[str, Any], self.client.get("team", "employees", employee_id))

    def update(self, employee_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update an employee.

        Args:
            employee_id: The employee ID
            data: Updated employee data

        Returns:
            The updated employee
        """
        return cast(Dict[str, Any], self.client.put("team", "employees", employee_id, data))

    def delete(self, employee_id: str) -> Dict[str, Any]:
        """
        Delete an employee.

        Args:
            employee_id: The employee ID

        Returns:
            The deletion response
        """
        return cast(Dict[str, Any], self.client.delete("team", "employees", employee_id))

    def list_time_trackings(self, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all time trackings for all employees.

        Args:
            params: Optional query parameters (e.g., page, limit, from, to)

        Returns:
            A list of time trackings
        """
        return cast(List[Dict[str, Any]], self.client.get("team", "timetracking", params=params))

    def get_time_tracking(self, tracking_id: str) -> Dict[str, Any]:
        """
        Get a specific time tracking.

        Args:
            tracking_id: The time tracking ID

        Returns:
            The time tracking details
        """
        return cast(Dict[str, Any], self.client.get("team", "timetracking", tracking_id))

    def update_time_tracking(self, tracking_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update a time tracking.

        Args:
            tracking_id: The time tracking ID
            data: Updated time tracking data

        Returns:
            The updated time tracking
        """
        return cast(Dict[str, Any], self.client.put("team", "timetracking", tracking_id, data))

    def delete_time_tracking(self, tracking_id: str) -> Dict[str, Any]:
        """
        Delete a time tracking.

        Args:
            tracking_id: The time tracking ID

        Returns:
            The deletion response
        """
        return cast(Dict[str, Any], self.client.delete("team", "timetracking", tracking_id))

    def list_employee_time_trackings(self, employee_id: str, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all time trackings for a specific employee.

        Args:
            employee_id: The employee ID
            params: Optional query parameters (e.g., page, limit, from, to)

        Returns:
            A list of time trackings for the employee
        """
        return cast(
            List[Dict[str, Any]],
            self.client.get(f"team", f"employees/{employee_id}/timetracking", params=params)
        )

    def create_employee_time_tracking(self, employee_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a time tracking for a specific employee.

        Args:
            employee_id: The employee ID
            data: Time tracking data

        Returns:
            The created time tracking
        """
        return cast(
            Dict[str, Any],
            self.client.post("team", f"employees/{employee_id}/timetracking", data)
        )

    def employee_clock_in(self, employee_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Clock in an employee.

        Args:
            employee_id: The employee ID
            data: Clock in data

        Returns:
            The clock in response
        """
        return cast(
            Dict[str, Any],
            self.client.post("team", f"employees/{employee_id}/clockin", data)
        )

    def employee_clock_out(self, employee_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Clock out an employee.

        Args:
            employee_id: The employee ID
            data: Clock out data

        Returns:
            The clock out response
        """
        return cast(
            Dict[str, Any],
            self.client.post("team", f"employees/{employee_id}/clockout", data)
        ) 