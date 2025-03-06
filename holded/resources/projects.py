"""
Projects resource for the Holded API.
"""
from typing import Any, Dict, List, Optional, cast

from . import BaseResource


class ProjectsResource(BaseResource):
    """
    Resource for interacting with the Projects API.
    """

    def list(self, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all projects.

        Args:
            params: Optional query parameters.

        Returns:
            A list of projects.
        """
        return cast(List[Dict[str, Any]], self.client.get("projects/projects", params=params))

    def create(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new project.

        Args:
            data: Project data.

        Returns:
            The created project.
        """
        return cast(Dict[str, Any], self.client.post("projects/projects", data=data))

    def get(self, project_id: str) -> Dict[str, Any]:
        """
        Get a specific project.

        Args:
            project_id: The project ID.

        Returns:
            The project.
        """
        return cast(Dict[str, Any], self.client.get(f"projects/projects/{project_id}"))

    def update(self, project_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update a project.

        Args:
            project_id: The project ID.
            data: Updated project data.

        Returns:
            The updated project.
        """
        return cast(Dict[str, Any], self.client.put(f"projects/projects/{project_id}", data=data))

    def delete(self, project_id: str) -> Dict[str, Any]:
        """
        Delete a project.

        Args:
            project_id: The project ID.

        Returns:
            A confirmation message.
        """
        return cast(Dict[str, Any], self.client.delete(f"projects/projects/{project_id}"))

    def get_summary(self, project_id: str) -> Dict[str, Any]:
        """
        Get a project summary.

        Args:
            project_id: The project ID

        Returns:
            The project summary
        """
        return cast(
            Dict[str, Any],
            self.client.get("projects", f"projects/{project_id}/summary")
        )

    def list_tasks(self, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all tasks.

        Args:
            params: Optional query parameters.

        Returns:
            A list of tasks.
        """
        return cast(List[Dict[str, Any]], self.client.get("projects/tasks", params=params))

    def create_task(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new task.

        Args:
            data: Task data.

        Returns:
            The created task.
        """
        return cast(Dict[str, Any], self.client.post("projects/tasks", data=data))

    def get_task(self, task_id: str) -> Dict[str, Any]:
        """
        Get a specific task.

        Args:
            task_id: The task ID.

        Returns:
            The task.
        """
        return cast(Dict[str, Any], self.client.get(f"projects/tasks/{task_id}"))

    def delete_task(self, task_id: str) -> Dict[str, Any]:
        """
        Delete a task.

        Args:
            task_id: The task ID.

        Returns:
            A confirmation message.
        """
        return cast(Dict[str, Any], self.client.delete(f"projects/tasks/{task_id}"))

    def list_project_time_trackings(self, project_id: str, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all time trackings for a specific project.

        Args:
            project_id: The project ID
            params: Optional query parameters (e.g., page, limit)

        Returns:
            A list of time trackings for the project
        """
        return cast(
            List[Dict[str, Any]],
            self.client.get("projects", f"projects/{project_id}/times", params=params)
        )

    def create_project_time_tracking(self, project_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a time tracking for a specific project.

        Args:
            project_id: The project ID
            data: Time tracking data

        Returns:
            The created time tracking
        """
        return cast(
            Dict[str, Any],
            self.client.post("projects", f"projects/{project_id}/times", data)
        )

    def get_project_time_tracking(self, project_id: str, tracking_id: str) -> Dict[str, Any]:
        """
        Get a specific time tracking for a project.

        Args:
            project_id: The project ID
            tracking_id: The time tracking ID

        Returns:
            The time tracking details
        """
        return cast(
            Dict[str, Any],
            self.client.get("projects", f"projects/{project_id}/times/{tracking_id}")
        )

    def update_project_time_tracking(self, project_id: str, tracking_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update a time tracking for a project.

        Args:
            project_id: The project ID
            tracking_id: The time tracking ID
            data: Updated time tracking data

        Returns:
            The updated time tracking
        """
        return cast(
            Dict[str, Any],
            self.client.put("projects", f"projects/{project_id}/times/{tracking_id}", data)
        )

    def delete_project_time_tracking(self, project_id: str, tracking_id: str) -> Dict[str, Any]:
        """
        Delete a time tracking for a project.

        Args:
            project_id: The project ID
            tracking_id: The time tracking ID

        Returns:
            The deletion response
        """
        return cast(
            Dict[str, Any],
            self.client.delete("projects", f"projects/{project_id}/times/{tracking_id}")
        )

    def list_all_time_trackings(self, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all time trackings across all projects.

        Args:
            params: Optional query parameters (e.g., page, limit)

        Returns:
            A list of all time trackings
        """
        return cast(
            List[Dict[str, Any]],
            self.client.get("projects", "times", params=params)
        )

    def list_times(self, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all time entries.

        Args:
            params: Optional query parameters.

        Returns:
            A list of time entries.
        """
        return cast(List[Dict[str, Any]], self.client.get("projects/times", params=params)) 