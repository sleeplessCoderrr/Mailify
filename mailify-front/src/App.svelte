<script lang="ts">
    import './app.css';
    import { Router, Route } from "svelte-routing";
    import Home from "./routes/Home.svelte";
    import Mailing from "./routes/Mailing.svelte";
</script>

<Router>
    <Route path="/">
        <Home/>
    </Route>
    <Route path="/mailing">
        <Mailing/>
    </Route>
</Router>

