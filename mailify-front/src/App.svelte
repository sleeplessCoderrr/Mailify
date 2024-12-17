<script lang="ts">
    import './app.css';
    import { Router, Route } from "svelte-routing";
    import Home from "./routes/Home.svelte";
    import EmailGenerator from "./routes/EmailGenerator.svelte";
</script>

<Router>
    <Route path="/">
        <Home/>
    </Route>
    <Route path="/mailing">
        <EmailGenerator/>
    </Route>
</Router>

