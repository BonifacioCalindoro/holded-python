"""
Asynchronous projects resource for the Holded API.
"""
from typing import Any, Dict, List, Optional, cast

from . import AsyncBaseResource


class AsyncProjectsResource(AsyncBaseResource):
    """
    Resource for interacting with the Projects API asynchronously.
    """

    def __init__(self, client):
        """Initialize the projects resource.

        Args:
            client: The Holded async client instance.
        """
        self.client = client
        self.base_path = "projects"

    async def list(self, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all projects asynchronously.

        Args:
            params: Optional query parameters.

        Returns:
            A list of projects.
        """
        result = await self.client.get(f"{self.base_path}/projects", params=params)
        return cast(List[Dict[str, Any]], result)

    async def create(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new project asynchronously.

        Args:
            data: Project data.

        Returns:
            The created project.
        """
        result = await self.client.post(f"{self.base_path}/projects", data=data)
        return cast(Dict[str, Any], result)

    async def get(self, project_id: str) -> Dict[str, Any]:
        """
        Get a specific project asynchronously.

        Args:
            project_id: The project ID.

        Returns:
            The project.
        """
        result = await self.client.get(f"{self.base_path}/projects/{project_id}")
        return cast(Dict[str, Any], result)

    async def update(self, project_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update a project asynchronously.

        Args:
            project_id: The project ID.
            data: Updated project data.

        Returns:
            The updated project.
        """
        result = await self.client.put(f"{self.base_path}/projects/{project_id}", data=data)
        return cast(Dict[str, Any], result)

    async def delete(self, project_id: str) -> Dict[str, Any]:
        """
        Delete a project asynchronously.

        Args:
            project_id: The project ID.

        Returns:
            A confirmation message.
        """
        result = await self.client.delete(f"{self.base_path}/projects/{project_id}")
        return cast(Dict[str, Any], result)

    async def get_summary(self, project_id: str) -> Dict[str, Any]:
        """
        Get a project summary asynchronously.

        Args:
            project_id: The project ID.

        Returns:
            The project summary.
        """
        result = await self.client.get(f"{self.base_path}/projects/{project_id}/summary")
        return cast(Dict[str, Any], result)

    async def list_tasks(self, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all tasks asynchronously.

        Args:
            params: Optional query parameters.

        Returns:
            A list of tasks.
        """
        result = await self.client.get(f"{self.base_path}/tasks", params=params)
        return cast(List[Dict[str, Any]], result)

    async def create_task(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new task asynchronously.

        Args:
            data: Task data.

        Returns:
            The created task.
        """
        result = await self.client.post(f"{self.base_path}/tasks", data=data)
        return cast(Dict[str, Any], result)

    async def get_task(self, task_id: str) -> Dict[str, Any]:
        """
        Get a specific task asynchronously.

        Args:
            task_id: The task ID.

        Returns:
            The task.
        """
        result = await self.client.get(f"{self.base_path}/tasks/{task_id}")
        return cast(Dict[str, Any], result)

    async def delete_task(self, task_id: str) -> Dict[str, Any]:
        """
        Delete a task asynchronously.

        Args:
            task_id: The task ID.

        Returns:
            A confirmation message.
        """
        result = await self.client.delete(f"{self.base_path}/tasks/{task_id}")
        return cast(Dict[str, Any], result)

    async def list_project_time_trackings(self, project_id: str, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all time trackings for a specific project asynchronously.

        Args:
            project_id: The project ID.
            params: Optional query parameters.

        Returns:
            A list of time trackings.
        """
        result = await self.client.get(f"{self.base_path}/projects/{project_id}/times", params=params)
        return cast(List[Dict[str, Any]], result)

    async def create_project_time_tracking(self, project_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new time tracking for a specific project asynchronously.

        Args:
            project_id: The project ID.
            data: Time tracking data.

        Returns:
            The created time tracking.
        """
        result = await self.client.post(f"{self.base_path}/projects/{project_id}/times", data=data)
        return cast(Dict[str, Any], result)

    async def get_project_time_tracking(self, project_id: str, tracking_id: str) -> Dict[str, Any]:
        """
        Get a specific time tracking for a project asynchronously.

        Args:
            project_id: The project ID.
            tracking_id: The time tracking ID.

        Returns:
            The time tracking.
        """
        result = await self.client.get(f"{self.base_path}/projects/{project_id}/times/{tracking_id}")
        return cast(Dict[str, Any], result)

    async def update_project_time_tracking(self, project_id: str, tracking_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update a time tracking for a project asynchronously.

        Args:
            project_id: The project ID.
            tracking_id: The time tracking ID.
            data: Updated time tracking data.

        Returns:
            The updated time tracking.
        """
        result = await self.client.put(f"{self.base_path}/projects/{project_id}/times/{tracking_id}", data=data)
        return cast(Dict[str, Any], result)

    async def delete_project_time_tracking(self, project_id: str, tracking_id: str) -> Dict[str, Any]:
        """
        Delete a time tracking for a project asynchronously.

        Args:
            project_id: The project ID.
            tracking_id: The time tracking ID.

        Returns:
            A confirmation message.
        """
        result = await self.client.delete(f"{self.base_path}/projects/{project_id}/times/{tracking_id}")
        return cast(Dict[str, Any], result)

    async def list_all_time_trackings(self, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all time trackings asynchronously.

        Args:
            params: Optional query parameters.

        Returns:
            A list of time trackings.
        """
        result = await self.client.get(f"{self.base_path}/times", params=params)
        return cast(List[Dict[str, Any]], result) 